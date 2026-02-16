(() => {
  const fab = document.getElementById("cb-fab");
  const overlay = document.getElementById("cb-overlay");
  const closeBtn = document.getElementById("cb-close");
  const form = document.getElementById("cb-form");
  const input = document.getElementById("cb-input");
  const messages = document.getElementById("cb-messages");
  const sendBtn = form?.querySelector("button[type='submit']");

  const open = () => {
    overlay.hidden = false;
    setTimeout(() => input?.focus(), 0);
    document.body.style.overflow = "hidden";
  };

  const close = () => {
    overlay.hidden = true;
    document.body.style.overflow = "";
  };

  const setInputEnabled = (enabled) => {
    if (!input || !sendBtn) return;
    input.disabled = !enabled;
    sendBtn.disabled = !enabled;
  };

  const addMsg = (text, who) => {
    const div = document.createElement("div");
    div.className = `cb__msg cb__msg--${who}`;
    div.textContent = text;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
    saveChat();
  };


  const addNodeMsg = (node, who = "bot") => {
    const wrap = document.createElement("div");
    wrap.className = `cb__msg cb__msg--${who}`;
    wrap.appendChild(node);
    messages.appendChild(wrap);
    messages.scrollTop = messages.scrollHeight;
  };

  const STORAGE_KEY = "cb_session_messages";

  const saveChat = () => {
    const data = Array.from(messages.querySelectorAll(".cb__msg"))
      .filter(el => !el.querySelector(".cb__quick")) // <-- ESCLUDE quick replies
      .map(el => {
        const who = el.classList.contains("cb__msg--user") ? "user" : "bot";
        const text = el.textContent || "";
        return { who, text };
      });

    sessionStorage.setItem("cb_session_messages", JSON.stringify(data));
  };


  const loadChat = () => {
    const raw = sessionStorage.getItem(STORAGE_KEY);
    if (!raw) return false;

    try {
      const data = JSON.parse(raw);
      messages.innerHTML = "";
      data.forEach(m => addMsg(m.text, m.who));
      return true;
    } catch {
      return false;
    }
  };


  // --- Quick replies ---
  const quickReplies = [
    { key: "what", label: "Cos’è Aidano?", reply: "Aidano è l’assistente della piattaforma: ti aiuta a trovare info e guidarti nelle funzioni principali. Con Aidano, puoi navigare tra le sezioni della piattaforma in maniera più accessibile. Il chatbot sarà sempre disponibile in basso a destra per supporto rapido. Per ulteriore supporto puoi consultare la sezione FAQ o contattare l’assistenza (quando sarà attiva!)." },
    { key: "free", label: "Ho un’altra domanda", reply: null }
  ];

  const renderQuickReplies = () => {
    const row = document.createElement("div");
    row.className = "cb__quick";

    quickReplies.forEach((q) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "cb__chip";
      b.textContent = q.label;

      b.addEventListener("click", () => {
        addMsg(q.label, "user");

        if (q.reply) {
          addMsg(q.reply, "bot");
          // input resta bloccato finché non clicchi "Ho un’altra domanda"
        } else {
          setInputEnabled(true);
          addMsg("Certo. Scrivimi pure la tua domanda qui sotto.", "bot");
          input.focus();
        }
      });


      row.appendChild(b);
    });

    addNodeMsg(row, "bot");
  };

  // --- Funzioni ---

  // --- Prima volta: saluto + quick replies (una sola volta) ---
  const restored = loadChat();
  const hasWelcomed = sessionStorage.getItem("cb_welcomed") === "1";

  if (!restored) {
    if (!hasWelcomed) {
      addMsg("Ciao! Io sono Aidano. Come posso aiutarti?", "bot");
      renderQuickReplies();
      setInputEnabled(false);
      sessionStorage.setItem("cb_welcomed", "1");
    } else {
      setInputEnabled(true);
    }
  } else {
    // se la chat è stata ripristinata, input come lo avevi lasciato:
    // scelta semplice: abilitalo sempre
    setInputEnabled(true);
  }


  // --- Event listeners ---
  fab.addEventListener("click", open);
  closeBtn.addEventListener("click", close);

  overlay.addEventListener("click", (e) => {
    if (e.target === overlay) close();
  });

  window.addEventListener("keydown", (e) => {
    if (!overlay.hidden && e.key === "Escape") close();
  });

	// prova backend 1 
	const API_URL = "/api/chat";

const getHistoryForBackend = () => {
  const raw = sessionStorage.getItem(STORAGE_KEY);
  if (!raw) return [];
  try {
    const data = JSON.parse(raw);
    // converte {who,text} -> {role,content}
    return data.map(m => ({
      role: m.who === "user" ? "user" : "assistant",
      content: m.text
    }));
  } catch {
    return [];
  }
};

const askBackend = async (text) => {
  const history = getHistoryForBackend();

  const r = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: text, history })
  });

  const data = await r.json().catch(() => ({}));

  if (!r.ok) {
    throw new Error(data.reply || ("HTTP " + r.status));
  }
  return data.reply || "";
};


  // mock chat senza backend
 form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if (!text) return;

  addMsg(text, "user");
  input.value = "";

  setInputEnabled(false);
  const typing = document.createElement("div");
  typing.className = "cb__msg cb__msg--bot";
  typing.textContent = "…";
  messages.appendChild(typing);
  messages.scrollTop = messages.scrollHeight;

  try {
    const reply = await askBackend(text);
    typing.remove();
    addMsg(reply || "Nessuna risposta dal server.", "bot");
  } catch (err) {
    typing.remove();
    addMsg("Errore di connessione al server.", "bot");
    console.error(err);
  } finally {
    setInputEnabled(true);
    input.focus();
  }
});

})();