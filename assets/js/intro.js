(() => {
  const overlay = document.getElementById("site-intro");
  if (!overlay || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  const navigation = performance.getEntriesByType("navigation")[0];
  const internalNavigation = document.referrer && new URL(document.referrer).origin === window.location.origin;
  if (navigation?.type === "back_forward" || (navigation?.type !== "reload" && internalNavigation)) return;

  const name = overlay.querySelector("[data-intro-text]");
  const text = name.dataset.introText;
  const glyphs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  const start = performance.now();
  let frame;
  let dismissed = false;
  overlay.hidden = false;

  const finish = () => {
    if (dismissed) return;
    dismissed = true;
    cancelAnimationFrame(frame);
    name.textContent = text;
    overlay.classList.add("is-leaving");
    document.removeEventListener("keydown", onKey);
    window.setTimeout(() => overlay.remove(), 450);
  };
  const onKey = (event) => {
    if (event.key === "Escape" || event.key === "Tab") finish();
  };
  const reveal = (now) => {
    const progress = Math.min((now - start) / 1000, 1);
    name.textContent = Array.from(text, (letter, index) =>
      letter === " " || index < progress * text.length ? letter : glyphs[Math.floor(Math.random() * glyphs.length)]
    ).join("");
    if (progress < 1 && !dismissed) frame = requestAnimationFrame(reveal);
  };
  frame = requestAnimationFrame(reveal);
  document.addEventListener("keydown", onKey);
  overlay.addEventListener("click", finish);
  window.setTimeout(finish, 2200);
})();
