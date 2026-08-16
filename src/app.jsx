import './assets/stylesheets/index.css'
import './assets/stylesheets/style.css'

import "./components/sidebar"
import { Sidebar } from './components/sidebar'
import { Spotlight } from "./components/spotlight"

export function App() {
  return (
    <section class="app-shell">
      <Sidebar />
      <section class="page-content">
        <section class="grid">
          <Spotlight item={{
            label: "title", 
            value: "value", 
            detail: "detail", 
            accent: "#ff7a59"
            }} />
            <Spotlight item={{
            label: "title", 
            value: "value", 
            detail: "detail", 
            accent: "#ffb347"
            }} />
            <Spotlight item={{
            label: "title", 
            value: "value", 
            detail: "detail", 
            accent: "#7ad3ff"
            }} />
        </section>
      </section>
    </section>
  )
}
