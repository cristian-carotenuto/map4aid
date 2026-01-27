/**
 * auth.js - Gestione dell'autenticazione lato View
 * 
 * Responsabilità:
 * - Simulare lo stato di login tramite sessionStorage (poiché il backend non inietta dati nelle pagine HTML)
 * - Aggiornare dinamicamente i pulsanti nell'header in base allo stato di autenticazione
 * - Fornire una funzione globale per la gestione degli errori UI
 * 
 * Nota: Questa è una simulazione di UI, non di sicurezza.
 * La sicurezza è gestita interamente dal backend (Flask + sessioni).
 */

// === UTILITÀ DI STATO ===

/**
 * Verifica se l'utente è loggato (basato su sessionStorage)
 * @returns {boolean} true se l'utente è loggato, false altrimenti
 */
function isLoggedIn() {
  return sessionStorage.getItem('isLoggedIn') === 'true';
}

/**
 * Restituisce l'email dell'utente loggato
 * @returns {string} email dell'utente o stringa vuota se non loggato
 */
function getUserEmail() {
  return sessionStorage.getItem('userEmail') || '';
}

/**
 * Salva lo stato di login in sessionStorage dopo un login riuscito
 * @param {string} email - Email dell'utente autenticato
 */
function saveLoginState(email) {
  sessionStorage.setItem('isLoggedIn', 'true');
  sessionStorage.setItem('userEmail', email);
}

/**
 * Rimuove lo stato di login da sessionStorage (logout)
 */
function clearLoginState() {
  sessionStorage.removeItem('isLoggedIn');
  sessionStorage.removeItem('userEmail');
}

// === GESTIONE ERRORI GLOBALI ===

/**
 * Mostra un messaggio di errore in un container specifico e lo nasconde automaticamente dopo 5 secondi
 * @param {string} containerId - ID dell'elemento HTML in cui mostrare il messaggio
 * @param {string} message - Messaggio di errore da visualizzare
 */
function showError(containerId, message) {
  const el = document.getElementById(containerId);
  if (el) {
    el.textContent = message;
    el.style.display = 'block';
    setTimeout(() => {
      el.style.display = 'none';
    }, 5000);
  }
}

// === AGGIORNAMENTO DELL'HEADER DINAMICO ===

/**
 * Aggiorna i pulsanti nell'header in base allo stato di autenticazione
 * Viene chiamata automaticamente all'avvio di ogni pagina
 */
function updateAuthButtons() {
  const container = document.getElementById('auth-buttons');
  if (!container) return;

  // "Donazione monetaria" è sempre visibile (RF#3: accessibile a tutti)
  if (isLoggedIn()) {
    container.innerHTML = `
      <a href="home.html" class="btn btn-light">Home</a>
      <a href="donazione.html" class="btn btn-light">Donazione monetaria</a>
      <span class="text-white me-2">Ciao, ${getUserEmail()}</span>
      <a href="profilo.html" class="btn btn-light">Profilo</a>
      <button class="btn btn-light" onclick="handleLogout()">Logout</button>
    `;
  } else {
    container.innerHTML = `
      <a href="home.html" class="btn btn-light">Home</a>
      <a href="donazione.html" class="btn btn-light">Donazione monetaria</a>
      <a href="login.html" class="btn btn-light">Login</a>
      <a href="register.html" class="btn btn-light">Sign In</a>
    `;
  }
}

// === GESTIONE DEL LOGOUT ===

/**
 * Esegue il logout chiamando il backend e pulendo lo stato locale
 * Reindirizza alla home dopo il logout
 */
async function handleLogout() {
  try {
    // Chiamata al backend per invalidare la sessione Flask
    await fetch('/logout', { method: 'POST' });
  } catch (error) {
    console.warn('Errore durante il logout:', error);
    // Procedi comunque con il logout locale
  } finally {
    clearLoginState();
    // Aggiorna l'header senza ricaricare la pagina
    if (typeof updateAuthButtons === 'function') {
      updateAuthButtons();
    }
    // Opzionale: reindirizza alla home
    window.location.href = 'home.html';
  }
}

// === INIZIALIZZAZIONE ===

/**
 * Inizializza l'header dinamico all'avvio di ogni pagina
 * Collegato all'evento DOMContentLoaded per garantire che il DOM sia pronto
 */
document.addEventListener('DOMContentLoaded', updateAuthButtons);
