# controllers/api_punti.py
from flask import Blueprint, request, jsonify, current_app
from sqlalchemy import text
from config import db
from controllers.permessi import require_roles
from controllers.prenotazione_control import is_craftable

api = Blueprint("api_punti", __name__)

def table_exists(conn, table_name: str) -> bool:
    q = text("SELECT name FROM sqlite_master WHERE type='table' AND name = :t")
    r = conn.execute(q, {"t": table_name}).fetchone()
    return r is not None

def _safe_row_get(row, index=None, key=None):
    """
    Recupera un valore da 'row' provando diversi metodi:
    - se row è tuple/list: usa index
    - se row ha attribute _mapping (SQLAlchemy Row): usa _mapping[key]
    - se row supporta accesso con chiave: prova row[key]
    - fallback: None
    """
    try:
        if isinstance(row, (tuple, list)):
            return row[index] if index is not None and index < len(row) else None
    except Exception:
        pass

    # SQLAlchemy Row e simili espongono ._mapping
    try:
        mapping = getattr(row, "_mapping", None)
        if mapping is not None:
            return mapping.get(key)
    except Exception:
        pass

    # try key access
    try:
        if key is not None:
            return row[key]
    except Exception:
        pass

    return None

def pragma_table_info(conn, table_name: str):
    """
    Normalizza PRAGMA table_info(...) in lista di dict con chiavi:
    cid, name, type, notnull, dflt_value, pk
    Gestisce righe tuple/list e Row mapping.
    """
    q = text(f"PRAGMA table_info('{table_name}')")
    res = conn.execute(q)
    rows = res.fetchall()
    parsed = []
    for r in rows:
        # typical tuple: (cid, name, type, notnull, dflt_value, pk)
        cid = _safe_row_get(r, index=0, key="cid")
        name = _safe_row_get(r, index=1, key="name")
        coltype = _safe_row_get(r, index=2, key="type")
        notnull = _safe_row_get(r, index=3, key="notnull")
        dflt = _safe_row_get(r, index=4, key="dflt_value")
        pk = _safe_row_get(r, index=5, key="pk")
        parsed.append({
            "cid": cid,
            "name": name,
            "type": coltype,
            "notnull": notnull,
            "dflt_value": dflt,
            "pk": pk
        })
    return parsed

def result_to_dicts(res):
    """
    Converte un risultato SQLAlchemy in lista di dict in modo robusto.
    Usa res.keys() per le colonne (se disponibile).
    """
    try:
        keys = list(res.keys())
    except Exception:
        # fallback: prendi colonne da first row se possibile
        rows_tmp = res.fetchall()
        if not rows_tmp:
            return []
        first = rows_tmp[0]
        try:
            keys = list(first._mapping.keys())
        except Exception:
            # as ultima risorsa, usare indici numerici
            keys = [f"col{i}" for i in range(len(first))]
        # ricostruisci risultato come se fosse stato appena letto
        out = []
        for row in rows_tmp:
            rowvals = []
            if isinstance(row, (tuple, list)):
                rowvals = list(row)
            else:
                try:
                    rowvals = [row._mapping.get(k) for k in keys]
                except Exception:
                    rowvals = list(row)
            out.append(dict(zip(keys, rowvals)))
        return out

    rows = res.fetchall()
    out = []
    for row in rows:
        # row può essere tuple o Row; zip funziona per entrambi
        out.append(dict(zip(keys, row)))
    return out


@api.route("/punti-distribuzione", methods=["GET"])
@api.route("/punti-distribuzione", methods=["GET"])
def get_punti_distribuzione():
    categoria = request.args.get("categoria", type=str)

    try:
        with db.engine.connect() as conn:
            # 1. Preparazione colonne (standard)
            pragma = pragma_table_info(conn, "punti_distribuzione")
            real_cols = [r["name"] for r in pragma if r["name"]]
            required_cols = ["id", "nome", "regione", "citta", "latitudine", "longitudine", "ente_erogatore_id"]
            select_cols = [c for c in required_cols if c in real_cols]

            if not select_cols:
                return jsonify({"error": "schema punti_distribuzione non valido"}), 500

            cols_sql = ", ".join(f"p.{c}" for c in select_cols)
            has_accettato = "accettato" in real_cols
            accettato_cond = "AND p.accettato = 1" if has_accettato else ""

            # --- CASO FILTRATO ---
            if categoria and all(table_exists(conn, t) for t in ("beni", "sotto_categorie", "macro_categorie")):
                cat_lower = categoria.lower().strip()

                # Se è alimentare, cerchiamo i punti che hanno ALMENO un bene alimentare
                # (per poi scremarli con is_craftable)
                search_term = f"%{cat_lower}%"
                if "alimen" in cat_lower: search_term = "%alimen%"

                sql = f"""
                    SELECT DISTINCT {cols_sql}
                    FROM punti_distribuzione p
                    JOIN beni b ON p.id = b.punto_distribuzione_id
                    JOIN sotto_categorie sc ON sc.id = b.sottocategoria_id
                    JOIN macro_categorie mc ON mc.id = sc.macro_categoria_id
                    WHERE lower(mc.nome) LIKE :cat 
                    AND b.quantita > 0 
                    {accettato_cond}
                """

                res = conn.execute(text(sql), {"cat": search_term})
                punti_candidati = result_to_dicts(res)

                # --- LOGICA RIGIDA PACCO ALIMENTARE ---
                if "alimen" in cat_lower:
                    punti_pacco_completo = []

                    for punto in punti_candidati:
                        # CHIAMATA ALLA LOGICA: is_craftable deve controllare se ci sono
                        # TUTTI i beni necessari (pasta, olio, latte, ecc.)
                        if is_craftable(punto['id']):
                            punti_pacco_completo.append(punto)

                    # RESTITUIAMO SOLO QUELLI CON PACCO COMPLETO
                    current_app.logger.info(
                        f"Filtro Alimentare: {len(punti_candidati)} candidati, {len(punti_pacco_completo)} validi.")
                    return jsonify({"data": punti_pacco_completo}), 200

                # Per le altre categorie (es. Vestiario), basta che ci sia almeno un bene
                return jsonify({"data": punti_candidati}), 200

            # --- CASO TUTTI I PUNTI ---
            else:
                where_clause = "WHERE accettato = 1" if has_accettato else ""
                sql = f"SELECT {', '.join(select_cols)} FROM punti_distribuzione {where_clause} ORDER BY id"
                res = conn.execute(text(sql))
                data = result_to_dicts(res)
                return jsonify({"data": data}), 200

    except Exception as e:
        current_app.logger.error("DB error on GET punti_distribuzione", exc_info=e)
        return jsonify({"error": "db_error", "message": str(e)}), 500

@api.route("/gestione-punto", methods=["POST"])
@require_roles("ente_erogatore")
def crea_punto():
    payload = request.get_json(silent=True)
    if not payload:
        return jsonify({"error": "invalid_request", "message": "JSON body richiesto"}), 400

    candidate_cols = [
        "nome",
        "regione",
        "citta",
        "giorni_apertura",
        "orario_apertura",
        "orario_chiusura",
        "latitudine",
        "longitudine",
        "ente_erogatore_id",
        "accettato"
    ]
    try:
        with db.engine.connect() as conn:
            pragma = pragma_table_info(conn, "punti_distribuzione")
            real_cols = [r["name"] for r in pragma if r["name"]]
            insert_cols = [c for c in candidate_cols if c in real_cols]

            if not insert_cols:
                current_app.logger.error("punti_distribuzione non contiene colonne valide per l'insert.")
                return jsonify({"error": "schema_invalido"}), 500

            params = {}
            for c in insert_cols:
                if c == "accettato":
                    params[c] = 0
                else:
                    params[c] = payload.get(c, None)

            cols_sql = ", ".join(insert_cols)
            vals_sql = ", ".join(f":{c}" for c in insert_cols)
            sql = f"INSERT INTO punti_distribuzione ({cols_sql}) VALUES ({vals_sql})"

            conn.execute(text(sql), params)
            conn.commit()
            last_id = conn.execute(text("SELECT last_insert_rowid()")).scalar()

            resp = {"message": "punto_creato", "id": int(last_id) if last_id is not None else None}
            if "accettato" in real_cols:
                resp["status"] = "pending"
                resp["note"] = "campo 'accettato' impostato a 0 (in attesa di approvazione)"
            else:
                resp["status"] = "created"
                resp["note"] = "schema DB non contiene il campo 'accettato' — il punto è stato creato senza flag di approvazione"

            return jsonify(resp), 201
    except Exception as e:
        current_app.logger.error("DB error on creating punto", exc_info=e)
        return jsonify({"error": "db_error", "message": str(e)}), 500


@api.route("/categorie", methods=["GET"])
def get_categorie():
    """Lista di tutte le sottocategorie raggruppate per macrocategoria"""
    from models.models import MacroCategoria
    macro_list = MacroCategoria.query.all()
    result = []
    for m in macro_list:
        for s in m.sotto_categorie:
            result.append({
                "id": s.id,
                "nome": s.nome,
                "macro": m.nome
            })
    return jsonify(result), 200
