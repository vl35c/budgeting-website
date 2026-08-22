import "../../../assets/stylesheets/style.css"
import "../../../assets/stylesheets/index.css"

import { bindThemeButton } from "../../ThemeButton";

export function SavingsModal({ onClose }) {
  function handle(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const filter = formData.get("savings-sort");
    const reverse = formData.get("savings-reverse");

    localStorage.setItem("savingsModalSortFilter", filter);
    localStorage.setItem("savingsModalReverseFilter", reverse);

    onClose();
  }

  return (
    <div class="bg-transparent" id="test">
      <article class="savings-modal modal">
        <div class="modal-header">
          <h2 class="modal-title">Reorder Savings Accounts</h2>
          <button class="close-button" onclick={onClose}> x </button>
        </div>
        <form id="savings-form" onSubmit={handle} method="POST">
          <label class="form-field">
            <span>Order by:</span>
            <select name="savings-sort">
              <option value="name">Name</option>
              <option value="current_amount">Amount</option>
              <option value="interest_rate">Interest Rate</option>
            </select>
          </label>
          <label class="form-field form-checkbox">
            <span>Reverse:</span>
            <input type="checkbox" name="savings-reverse" />
          </label>
          <label class="form-submit">
            <input type="submit" value="Reorder" class="submit-button" />
          </label>
        </form>
      </article>
    </div>
  )
}