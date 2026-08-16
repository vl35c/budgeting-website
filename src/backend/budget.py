from expense import Expense
from savings import SavingsAccount


class Budget:
  def __init__(
      self, 
      income: float=0, 
      savings_accounts: list[SavingsAccount]=[],
      expenses: list[Expense]=[]
      ):
    """
    income: float - monthly income
    savings_accounts - list of savings accounts user has
    """
    self.income = income
    self.savings_accounts = savings_accounts
    self.expenses = expenses

  def savings_to_web_payload(self):
    """Returns savings accounts as a JSON web payload"""
    return {
      "savings": [acc.to_web_payload() for acc in self.savings_accounts]
    }

  def get_total_savings(self) -> float:
    """Sums total of all savings accounts"""
    return sum([acc.current_amount for acc in self.savings_accounts])

  def get_amount_of_savings_accounts(self) -> int:
    """Returns the amount of savings account a user has"""
    return len(self.savings_accounts)

  def get_total_expenses(self) -> float:
    """Sums total of all expenses per month"""
    return sum([expense.monthly_amount for expense in self.expenses])

  def get_income_buffer(self) -> float:
    """Gets amount of months current savings would cover based on expenses"""
    return round(self.get_total_savings() / self.get_total_expenses(), 1)