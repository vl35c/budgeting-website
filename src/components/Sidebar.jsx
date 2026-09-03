import "../assets/stylesheets/style.css"
import { CurrencyButton } from "./CurrencyButton.jsx"
import { ThemeButton } from "./ThemeButton"

export function Sidebar() {
  return (
    <aside class="sidebar">
      <ThemeButton />
      <nav class="sidebar-nav">
        <a class="sidebar-button active" href="">Home</a>
        <a class="sidebar-button" href="">Income and Expense</a>
        <a class="sidebar-button" href="">Goal Setting</a>
      </nav>
      <CurrencyButton />
    </aside>
  )
}
