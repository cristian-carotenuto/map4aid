/**
 * auth.js - Gestione dell'autenticazione lato View
 *
 * Responsabilità:
 * - Simulare lo stato di login tramite sessionStorage
 * - Aggiornare dinamicamente i pulsanti nell'header
 * - Fornire funzioni globali showError / showSuccess per la UI
 *
 * Nota: Questa è una simulazione di UI, non di sicurezza.
 * La sicurezza è gestita interamente dal backend (Flask + sessioni).
 */

// === UTILITÀ DI STATO ===

/**
 * Verifica se l'utente è loggato
 * @returns {boolean}
 */
function isLoggedIn() {
  return sessionStorage.getItem('isLoggedIn') === 'true';
}

/**
 * Restituisce l'email dell'utente loggato
 * @returns {string}
 */
function getUserEmail() {
  return sessionStorage.getItem('userEmail') || '';
}

function getUserRole() {
  return sessionStorage.getItem('userRole') || '';
}

/**
 * Salva lo stato di login in sessionStorage
 * @param {string} email
 * @param {string} ruolo
 */
function saveLoginState(email, ruolo) {
  sessionStorage.setItem('isLoggedIn', 'true');
  sessionStorage.setItem('userEmail', email);
  sessionStorage.setItem('userRole', ruolo);
}

/**
 * Rimuove lo stato di login da sessionStorage
 */
function clearLoginState() {
  sessionStorage.removeItem('isLoggedIn');
  sessionStorage.removeItem('userEmail');
  sessionStorage.removeItem("userRole");
}

// === GESTIONE ERRORI / SUCCESSI GLOBALI ===

/**
 * Mostra un messaggio di errore in un container specifico (auto-hide 5s)
 * @param {string} containerId - ID dell'elemento HTML
 * @param {string} message - Messaggio di errore
 */
function showError(containerId, message) {
  const el = document.getElementById(containerId);
  if (!el) return;
  el.textContent = message;
  el.style.display = 'block';
  el.classList.remove('text-success');
  el.classList.add('text-danger');
  setTimeout(() => { el.style.display = 'none'; }, 5000);
}

/**
 * Mostra un messaggio di successo in un container specifico (auto-hide 5s)
 * @param {string} containerId - ID dell'elemento HTML
 * @param {string} message - Messaggio di successo
 */
function showSuccess(containerId, message) {
  const el = document.getElementById(containerId);
  if (!el) return;
  el.textContent = message;
  el.style.display = 'block';
  el.classList.remove('text-danger');
  el.classList.add('text-success');
  setTimeout(() => { el.style.display = 'none'; }, 5000);
}

// === AGGIORNAMENTO HEADER DINAMICO ===

/**
 * Aggiorna i pulsanti nell'header in base allo stato di autenticazione
 */
function updateAuthButtons() {
  const container = document.getElementById('auth-buttons');
  if (!container) return;

  // Escape sicuro dell'email per prevenire XSS
  const safeEmail = getUserEmail().replace(/</g, '&lt;').replace(/>/g, '&gt;');
  let role = getUserRole();

  if (isLoggedIn() && role === 'donatore') {
    container.innerHTML = `
      <a href="home.html" class="btn btn-light">Home</a>
      <a href="donazione.html" class="btn btn-light">Donazione monetaria</a>
      <a href="donazione-beni.html" class="btn btn-light">Donazione beni</a>
      <a href="profilo.html" class="btn btn-light">Profilo</a>
      <button class="btn btn-light" onclick="handleLogout()">Logout</button>
    `;
  } else if (isLoggedIn()) {
    container.innerHTML = `
      <a href="home.html" class="btn btn-light">Home</a>
      <a href="donazione.html" class="btn btn-light">Donazione monetaria</a>
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
 */
async function handleLogout() {
  try {
    // Usa credentials: 'same-origin' per inviare i cookie di sessione
    await fetch('/auth/logout', {
      method: 'POST',
      credentials: 'same-origin'
    });
  } catch (error) {
    console.warn('Errore durante il logout:', error);
  } finally {
    clearLoginState();
    if (typeof updateAuthButtons === 'function') updateAuthButtons();
    window.location.href = 'home.html';
  }
}

// === ESPOSIZIONE GLOBALE (per compatibilità con script inline) ===
window.showError = showError;
window.showSuccess = showSuccess;
window.handleLogout = handleLogout;
window.updateAuthButtons = updateAuthButtons;
window.isLoggedIn = isLoggedIn;
window.getUserEmail = getUserEmail;
window.saveLoginState = saveLoginState;
window.clearLoginState = clearLoginState;

// === INIZIALIZZAZIONE ===
document.addEventListener('DOMContentLoaded', updateAuthButtons);
