function isLoggedIn() {
  return sessionStorage.getItem('isLoggedIn') === 'true';
}

function getUserEmail() {
  return sessionStorage.getItem('userEmail') || '';
}

function saveLoginState(email) {
  sessionStorage.setItem('isLoggedIn', 'true');
  sessionStorage.setItem('userEmail', email);
}

function clearLoginState() {
  sessionStorage.removeItem('isLoggedIn');
  sessionStorage.removeItem('userEmail');
}

function updateAuthButtons() {
  const container = document.getElementById('auth-buttons');
  if (!container) return;

  if (isLoggedIn()) {
    container.innerHTML = `
      <a href="donazione.html" class="btn btn-light">Donazione monetaria</a>
      <a href="profilo.html" class="btn btn-light">Profilo</a>
      <button class="btn btn-light" onclick="handleLogout()">Logout</button>
    `;
  } else {
    container.innerHTML = `
      <a href="donazione.html" class="btn btn-light">Donazione monetaria</a>
      <a href="APP.html" class="btn btn-light">APP</a>
      <a href="login.html" class="btn btn-light">Login</a>
      <a href="register.html" class="btn btn-light">Sign In</a>
    `;
  }
}


async function handleLogout() {
  try {
    await fetch('/logout', { method: 'POST' });
  } catch (error) {
    console.warn('Errore durante il logout:', error);
  } finally {
    clearLoginState();
    window.location.href = 'home.html';
  }
}

document.addEventListener('DOMContentLoaded', () => {
  updateAuthButtons();
});
