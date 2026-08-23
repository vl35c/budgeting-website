import "../../../assets/stylesheets/style.css"
import "../../../assets/stylesheets/index.css"

import { createPortal } from "preact/compat"
import { useEffect, useState } from "react"

export function IncomeBufferModal({ onClose }) {
  const [data, setData] = useState(null);

  function isBufferAccount(account) {
    for (let index in data.accounts) {
      if (data.accounts[index].name === account.name) { return true; }
    }
    return false;
  }

  function handle(event) {
    event.preventDefault();

    let payload = "";

    const formData = new FormData(event.target);
    for (let index in data.savings) {
      let name = data.savings[index].name
      if (formData.get(name) != null) {
        payload += `${name};`  // ; delimiter
      }
    }

    fetch(`api/budget/update-buffer-accounts?accounts=${payload}`);
    onClose();
  }

  useEffect(() => {
    (async () => {
      const result = await fetch("/api/budget/buffer-accounts")
        .then((res) => res.json())
        .catch((err) => console.log(err))
      setData(result);
    })();
  }, []);

  if (!data) {
    return <>
      {createPortal(
        <div class="bg-transparent">
          <article class="modal">
            <div class="modal-header">
              <h2>Loading...</h2>
            </div>
          </article>
        </div>, document.body
      )}
    </>
  }

  return (
    <>
    {createPortal(
      <div class="bg-transparent">
        <article class="modal">
          <div class="modal-header">
            <h2>Select Accounts</h2>
            <button onClick={onClose} class="close-button">x</button>
          </div>
          <form onSubmit={handle} method="POST">
            {data.savings.map(acc => <label class="form-field form-checkbox">
              <span>{acc.name}</span>
              {isBufferAccount(acc) ? 
              <input type="checkbox" name={acc.name} checked /> : 
              <input type="checkbox" name={acc.name} />}
            </label>)}
            <label class="form-submit">
              <input type="submit" class="submit-button" value="Filter Accounts" />
            </label>
          </form>
        </article>
      </div>, document.body
    )}
    </>
  )
}