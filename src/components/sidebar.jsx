import "../assets/stylesheets/style.css"
import "../components/ThemeButton"
import { ThemeButton } from "../components/ThemeButton"

export function Sidebar() {
  return (
    <aside class="sidebar">
      <ThemeButton />
      <nav class="sidebar-nav">
        <a class="sidebar-button active" href="">Home</a>
        <a class="sidebar-button" href="">Income and Expense</a>
        <a class="sidebar-button" href="">Goal Setting</a>
      </nav>
    </aside>
  )
}