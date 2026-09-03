import { useEffect, useState } from "react";

import "../../assets/stylesheets/style.css"
import "../../assets/stylesheets/index.css"

import { IncomeBufferModal } from "./modals/IncomeBufferModal";

const modals = new Map([
  ["IncomeBufferModal", <IncomeBufferModal />]
])

export function Spotlight({ spotlight_id }) {
  const [data, setData] = useState(null);
  const [modal, setModal] = useState(null);
  const [open, setOpen] = useState(false);
  const [localUpdate, setLocalUpdate] = useState(0);

  const openModal = () => { setOpen(true); }
  const closeModal = () => { setOpen(false); }

  useEffect(async () => {
    const element = document.getElementById("currency-select");
    element.addEventListener("change", () => {
      setLocalUpdate(localUpdate + 1);      
    })
  }, [])

  useEffect(async () => {
    const result = await fetch(`/api/spotlight/${spotlight_id}`)
      .then((res) => res.json())
      .catch((err) => console.log(err))
    setData(result);
  }, [
      localStorage.getItem("flag"),
      localUpdate,
      ]);

  if (data && !modal) { 
    if (Object.hasOwn(data, "modal")) {
      let comp = modals.get(data["modal"]);
      comp.props["onClose"] = closeModal;
      setModal(comp);
    }
  }

  return (
    <>
    <article class="card">
      <p class="eyebrow">
        <span>{data ? data.label : "Loading..."}</span>
        {modal && <button class="eyebrow-button pos-top-right" style="--pad: 12px;" onClick={openModal}>⚙️</button>}
      </p>
      <h3 class="numerical">{data ? data.value : ""}</h3>
      <p class="detail">{data ? data.detail : ""}</p>
    </article>

    {open && modal}
    </>
  )
}
