from budget import Budget
from util import formatGBP, formatPlural


class SpotlightData:
  def __init__(self, budget: Budget=None):
    self.budget = budget
    self.__templates = {
      "savings": self.__savings,
      "buffer": self.__buffer,
      "income": self.__income,
    }

  def get_data(self, template: str="") -> dict:
    """Returns template data for spotlight"""
    if template not in self.__templates:
      return {}
    return self.__templates[template]()

  def check_data(self, template: str=""):
    if template in self.__templates:
      return True
    return False

  def __savings(self):
    return {
      "label": "total savings",
      "value": formatGBP(self.budget.get_total_savings()),
      "detail": f"In {formatPlural(self.budget.get_amount_of_savings_accounts(), 'account', 'accounts')}"
    }

  def __buffer(self):
    return {
      "label": "income buffer",
      "value": f"{self.budget.get_income_buffer()} months",
      "detail": "Equivalent of spend for period",
      "modal": "IncomeBufferModal"
    }

  def __income(self):
    return {
      "label": "monthly income",
      "value": formatGBP(self.budget.income),
      "detail": ""
    }
