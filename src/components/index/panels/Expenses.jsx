import "../../../assets/stylesheets/style.css"
import "../../../assets/stylesheets/index.css"

import { useState, useEffect } from "react"

export function ExpensesPanel() {
  const [data, setData] = useState(null);

  useEffect(() => {
    (async () => {
      const result = await fetch("/api/budget/expenses?limit=4")
        .then((res) => res.json())
        .catch((err) => console.error(err));

      setData(result);
    })();
  }, []);

  if (!data) {
    return (
      <article class="detail-panel">
        <p class="eyebrow">Top Expenses</p>
      </article>
    )
  }

  return (
    <article class="detail-panel">
      <p class="eyebrow">Top Expenses</p>
      <ul class="detail-list">
        {data.expenses.map(expense => 
          <li>
            <span>{expense.name}</span>
            <strong class="numerical">{expense.monthly_amount}</strong>
          </li>
        )}
      </ul>
    </article>
  )
}
