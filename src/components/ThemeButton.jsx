import "../assets/stylesheets/index.css";

export function bindThemeButton() {
  if (!themeButton) { return; }

  themeButton.addEventListener("click", function () {
    document.body.classList.toggle("light-mode");
    localStorage.setItem("theme", localStorage.getItem("theme") === "light-mode" ? "dark-mode" : "light-mode");
  })
}

export function ThemeButton() {
  return (
    <button id="themeButton" class="theme-toggle" type="button" aria-label="Toggle Theme">
      <span id="themeButtonIcon">☀︎</span>
    </button>
  );
};