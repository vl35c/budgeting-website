import "../../../assets/stylesheets/style.css"
import "../../../assets/stylesheets/index.css"

export function SavingsModal({ onClose }) {
  return (
    <div class="bg-transparent">
      <article class="savings-modal modal">
        <div class="modal-header">
          <h2 class="modal-title">Reorder Savings Accounts</h2>
          <button class="close-button" onclick={onClose}> x </button>
        </div>
        <form>
          <label class="form-field">
            <span>Order by:</span>
            <select>
              <option value="name">Name</option>
              <option value="amount">Amount</option>
              <option value="interest-rate">Interest Rate</option>
            </select>
          </label>
          <label class="form-submit">
            <input type="submit" value="Reorder" class="submit-button" />
          </label>
        </form>
      </article>
    </div>
  )
}