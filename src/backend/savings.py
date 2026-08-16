from util import formatGBP


class SavingsAccount:
  def __init__(self, name: str="", current_amount: float=0, interest_rate: float=0):
    """
    name: str - name of account
    current_amount: float - amount of money currently in savings account
    interest_rate: float - % interest rate of savings account (3% -> 3 not 0.03)
    """
    self.name = name
    self.current_amount = current_amount
    self.interest_rate = interest_rate

  def to_web_payload(self):
    """Returns object as a JSON payload"""
    return {
      "name": self.name,
      "current_amount": formatGBP(self.current_amount),
      "interest_rate": f"{self.interest_rate}%",
    }