import './assets/stylesheets/index.css'
import './assets/stylesheets/style.css'

import { useState } from 'react'

import { SavingsPanel } from './components/index/panels/Savings'
import { Sidebar } from './components/Sidebar'
import { Spotlight } from "./components/index/Spotlight"
import { SavingsModal } from './components/index/modals/SavingsModal'

export function App() {
  const [open, setOpen] = useState(false);

  const openModal = () => { setOpen(true); }
  const closeModal = () => { setOpen(false); }

  return (
    <>
    <section class="app-shell">
      <Sidebar />
      <section class="page-content">
        <section class="grid">
          <Spotlight spotlight_id="income" />
          <Spotlight spotlight_id="savings" />
          <Spotlight spotlight_id="buffer" />
        </section>
        <section class="panel-grid">
          <SavingsPanel onSettingsClick={openModal} />
        </section>
      </section>
    </section>

    {open && <SavingsModal onClose={closeModal} />}
    </>
  )
}

export default App;
