import { render } from 'preact'
import { Suspense, lazy } from "preact/compat"

import { App } from "./app.jsx"
import { bindThemeButton, syncThemeButton } from "./components/ThemeButton.jsx"

function syncTheme() {
  if (localStorage.getItem("theme") === "light-mode") {
    // toggle light mode on
    document.body.classList.add("light-mode");
  }

  syncThemeButton();
}

render(<App />, document.getElementById('app'))

bindThemeButton();
syncTheme();
