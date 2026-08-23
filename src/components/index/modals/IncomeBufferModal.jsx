import "../../../assets/stylesheets/style.css"
import "../../../assets/stylesheets/index.css"
import { createPortal } from "preact/compat"

export function IncomeBufferModal({ onClose }) {
  return (
    <>
    {createPortal(
      <div class="bg-transparent">
        <article class="modal savings-modal">
          <div class="modal-header">
            <h2>Hello World</h2>
            <button onClick={onClose} class="close-button">x</button>
          </div> 
        </article>
      </div>, document.body
    )}
    </>
  )
}