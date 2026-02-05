(() => {
  // 1) CSS
  const cssHref = "../chatbot/css/chatbot.css";
  if (!document.querySelector(`link[href="${cssHref}"]`)) {
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = cssHref;
    document.head.appendChild(link);
  }

  // 2) HTML widget
  if (!document.getElementById("chatbot-widget")) {
    const wrapper = document.createElement("div");
    wrapper.innerHTML = `
      <div id="chatbot-widget" class="cb">
        <button id="cb-fab" class="cb__fab" aria-label="Apri chatbot">
          <img src="../chatbot/imgs/min_aidano.png" alt="Chatbot" class="cb__fabIcon">
        </button>

        <div id="cb-overlay" class="cb__overlay" hidden>
          <div class="cb__panel" role="dialog" aria-modal="true" aria-label="Chatbot">
            <div class="cb__header">
              <div class="cb__headerLeft">
                <img src="../chatbot/imgs/min_aidano.png" alt="" class="cb__headerIcon">
                <span class="cb__title">Aidano</span>
              </div>
              <button id="cb-close" class="cb__close" aria-label="Chiudi">✕</button>
            </div>

            <div id="cb-messages" class="cb__messages"></div>

            <form id="cb-form" class="cb__inputBar">
              <input id="cb-input" class="cb__input" type="text" placeholder="Scrivi un messaggio..." autocomplete="off">
              <button class="cb__send" type="submit">Invia</button>
            </form>
          </div>
        </div>
      </div>
    `.trim();

    document.body.appendChild(wrapper.firstElementChild);
  }

  // 3) JS logica chatbot
  const jsSrc = "../chatbot/js/chatbot.js";
  if (!document.querySelector(`script[src="${jsSrc}"]`)) {
    const s = document.createElement("script");
    s.src = jsSrc;
    document.body.appendChild(s);
  }
})();
