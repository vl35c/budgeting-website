import "../assets/stylesheets/index.css"

export function ThemeButton() {
  return (
    <button id="themeButton" class="theme-toggle" type="button" aria-label="Toggle Theme">
      <span id="themeButtonIcon">☀︎</span>
    </button>
  )
}