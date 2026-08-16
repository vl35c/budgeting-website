def formatGBP(amount: float) -> str:
  """Returns float in format £XX.XX"""
  try:
    return f"£{amount:,.2f}"
  except TypeError:
    raise Exception(f"Amount {amount} is ({type(amount)}) not (float)")


def formatPlural(amount: int, singular: str, plural: str):
  """Returns singular if amount is 1, else plural"""
  return f"{amount} {singular}" if amount == 1 else f"{amount} {plural}"