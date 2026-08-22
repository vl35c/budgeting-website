import { useState, useEffect } from "react";

import "../../../assets/stylesheets/style.css"
import "../../../assets/stylesheets/index.css"

function getInterestRateBand(rate) {
  if (rate < 4) {
    return "interest-band-low";
  } else if (rate >= 4 && rate < 8) {
    return "interest-band-medium";
  } else {
    return "interest-band-high";
  }
}

export function SavingsPanel({ onSettingsClick }) {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    (async () => {
      let sortFilter = localStorage.getItem("savingsModalSortFilter");
      const result = await fetch(`/api/budget/savings-accounts?attr=${sortFilter}`)
        .then((res) => res.json())
        .catch((err) => console.log(err))
      setData(result);
    })()
  }, [localStorage.getItem("savingsModalSortFilter")]);

  if (!data) { return <div>Loading...</div> }

  return (
    <article class="detail-panel">
      <p class="eyebrow">
        Savings Accounts
        <button onclick={onSettingsClick} class="eyebrow-button pos-top-right" style="--pad: 12px;">⚙️</button>
      </p>
      {data.savings.map(acc => 
        <ul class="detail-list">
          <li>
            <span>
              {acc.name}
              <span class={[getInterestRateBand(acc.interest_rate_numerical), "savings-interest", "numerical"].join(" ")}>
                {acc.interest_rate}
              </span>
            </span>
            <strong class="numerical">{acc.current_amount}</strong>
          </li>
        </ul>
      )}
    </article>
  )
}