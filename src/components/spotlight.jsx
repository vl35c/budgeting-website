import { useEffect, useState } from "react";

import "../assets/stylesheets/style.css"
import "../assets/stylesheets/index.css"

export function Spotlight({ spotlight_id }) {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    (async () => {
      const result = await fetch(`/api/spotlight/${spotlight_id}`)
        .then((res) => res.json())
        .catch((err) => console.log(err))
      setData(result);
    })()
  }, []);

  return (
    <article class="card">
      <p class="eyebrow">{data ? data.label : "Loading..."}</p>
      <h3 class="numerical">{data ? data.value : ""}</h3>
      <p class="detail">{data ? data.detail : ""}</p>
    </article>
  )
}