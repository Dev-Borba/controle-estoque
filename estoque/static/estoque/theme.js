(() => {
  const raiz = document.documentElement;
  const botao = document.getElementById("theme-toggle");
  const texto = document.getElementById("theme-toggle-text");

  if (!botao || !texto) return;

  const atualizarBotao = () => {
    const escuro = raiz.dataset.theme === "dark";
    const destino = escuro ? "claro" : "escuro";

    texto.textContent = `Tema ${destino}`;

    botao.setAttribute(
      "aria-label",
      `Ativar tema ${destino}`
    );

    botao.title = `Ativar tema ${destino}`;
  };

  const aplicarTema = (tema) => {
    raiz.dataset.theme = tema;
    atualizarBotao();
  };

  botao.addEventListener("click", () => {
    const tema = raiz.dataset.theme === "dark"
      ? "light"
      : "dark";

    aplicarTema(tema);

    try {
      localStorage.setItem("controle-estoque-tema", tema);
    } catch {
      // A troca funciona mesmo se o navegador bloquear o armazenamento.
    }
  });

  window.addEventListener("storage", (event) => {
    if (
      event.key === "controle-estoque-tema" &&
      (event.newValue === "light" || event.newValue === "dark")
    ) {
      aplicarTema(event.newValue);
    }
  });

  atualizarBotao();
  botao.hidden = false;
})();