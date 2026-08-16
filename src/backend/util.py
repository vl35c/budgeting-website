def formatGBP(amount: float) -> str:
  """Returns float in format £XX.XX"""
  try:
    return f"£{amount:,.2f}"
  except TypeError:
    raise Exception(f"Amount {amount} is ({type(amount)}) not (float)")