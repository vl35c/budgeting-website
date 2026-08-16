import { useState, useEffect } from "react";

import "../../../assets/stylesheets/style.css"
import "../../../assets/stylesheets/index.css"

export function SavingsPanel() {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    (async () => {
      const result = await fetch(`/api/budget/savings-accounts`)
        .then((res) => res.json())
        .catch((err) => console.log(err))
      setData(result);
    })()
  }, []);

  if (!data) { return <div>Loading...</div> }

  return (
    <article class="detail-panel">
      <p class="eyebrow">Savings Accounts</p>
      {data.savings.map(acc => 
        <ul class="detail-list">
          <li>
            <span>{acc.name}</span>
            <strong class="numerical">{acc.current_amount}</strong>
          </li>
        </ul>
      )}
    </article>
  )
}