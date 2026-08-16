import { useEffect, useState } from 'react'
import './assets/stylesheets/index.css'
import './assets/stylesheets/style.css'

import "./components/Sidebar"
import { Sidebar } from './components/Sidebar'
import { Spotlight } from "./components/Spotlight"

export function App() {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    (async () => {
      const result = await fetch("/api/spotlight").then((res) => res.json());
      setData(result);
    })()
  }, []);

  if (!data) { return <div>Loading...</div> }

  return (
    <section class="app-shell">
      <Sidebar />
      <section class="page-content">
        <section class="grid">
          <Spotlight item={{
            label: data["info"].label,
            value: data.info.value, 
            detail: data.info.detail, 
            accent: data.info.accent,
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

export default App;
