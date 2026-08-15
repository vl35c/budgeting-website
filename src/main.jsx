import { render } from 'preact'
import { App } from './app.jsx'

import { bindThemeButton } from "./components/ThemeButton.jsx"

function syncTheme() {
  if (localStorage.getItem("theme") === "light-mode") {
    // toggle light mode on
    document.body.classList.add("light-mode");
  }
}


render(<App />, document.getElementById('app'))

syncTheme();
bindThemeButton();
