import "../assets/stylesheets/style.css"

import { useState, useEffect } from "react"


export function CurrencyButton() {
  const [data, setData] = useState();

  useEffect(() => {
    (async () => {
      const result = await fetch("/api/ccy/get_all_currencies")
        .then((res) => res.json())
        .catch((err) => console.error(err));

      setData(result);
    })();
  }, []);

  useEffect(() => {
    const element = document.getElementById("currency-select");
    element.addEventListener("change", (event) => {
      const ccy = element.value;

      (async () => {
        await fetch(`/api/ccy/set_currency?ccy=${ccy}`);
      })();
    })
  }, []);

  return (
    <select id="currency-select" class="sidebar-button currency-button" name="Change Currency">
      {data && data.currencies.map(ccy =>
        <option name="{ccy.code}">{ccy.code}</option>
      )}
    </select>
  )
}
