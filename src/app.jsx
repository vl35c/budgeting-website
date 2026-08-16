import './assets/stylesheets/index.css'
import './assets/stylesheets/style.css'

import "./components/Sidebar"
import { SavingsPanel } from './components/index/panels/Savings'
import { Sidebar } from './components/Sidebar'
import { Spotlight } from "./components/index/Spotlight"

export function App() {
  return (
    <section class="app-shell">
      <Sidebar />
      <section class="page-content">
        <section class="grid">
          <Spotlight spotlight_id="income" />
          <Spotlight spotlight_id="savings" />
          <Spotlight spotlight_id="buffer" />
        </section>
        <section class="panel-grid">
          <SavingsPanel />
        </section>
      </section>
    </section>
  )
}

export default App;
