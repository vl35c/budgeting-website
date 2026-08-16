import "../assets/stylesheets/style.css"
import "../assets/stylesheets/index.css"

export function Spotlight({ item }) {
  const accentColor = "--accent:" + item.accent;

  return (
    <article class="card" style={accentColor}>
      <p class="eyebrow">{item.label}</p>
      <h3 class="numerical">{item.value}</h3>
      <p class="detail">{item.detail}</p>
    </article>
  )
}