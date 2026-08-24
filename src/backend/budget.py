from expense import Expense
from savings import SavingsAccount
from user_settings import UserSettings


class Budget:
  def __init__(
      self, 
      income: float=0, 
      savings_accounts: list[SavingsAccount]=[],
      expenses: list[Expense]=[],
      user_settings: UserSettings=None
      ):
    """
    income: float - monthly income
    savings_accounts - list of savings accounts user has
    """
    self.income = income
    self.savings_accounts = savings_accounts
    self.expenses = expenses
    self.user_settings = user_settings

  def init_user_settings(self) -> None:
    """Set up all user settings for use"""
    self.user_settings.savings_accounts_for_buffer = self.savings_accounts

  def update_savings_accounts_for_buffer(self, accounts: list[str]) -> None:
    """Takes in a list of account names, and updates all accounts which contribute to income buffer"""
    self.user_settings.savings_accounts_for_buffer = [self.get_savings_account_by_name(name) for name in accounts]
    print(f"New Buffer Accounts: {[acc.name for acc in self.user_settings.savings_accounts_for_buffer]}")

  def savings_to_web_payload(self, attr: str="current_amount", reverse: bool=True) -> dict:
    """
    Returns savings accounts as a JSON web payload
    attr: str - attribute of which to sort by - default is savings amount
    reverse: bool - whether to reverse the sort - generally true for numbers, false for strings
    """
    if attr and not hasattr(SavingsAccount(), attr):
      raise Exception(f"SavingsAccount does not contain attribute {attr}")

    return {
      "savings": [acc.to_web_payload() for acc in sorted(self.savings_accounts, key=lambda acc: getattr(acc, attr), reverse=reverse)]
    }

  def savings_buffer_to_web_payload(self, attr: str="name", reverse: bool=False) -> dict:
    """
    Returns all savings accounts used in calculating income buffer
    attr: str - attribute of which to sort by - default is savings amount
    reverse: bool - whether to reverse the sort - generally true for numbers, false for strings
    """
    if attr and not hasattr(SavingsAccount(), attr):
      raise Exception(f"SavingsAccount does not contain attribute {attr}")

    return {
      "accounts": [acc.to_web_payload() for acc in sorted(
        self.user_settings.savings_accounts_for_buffer,
        key=lambda acc: getattr(acc, attr),
        reverse=reverse
      )]
    }

  def get_total_savings(self, accs: list[SavingsAccount]=None) -> float:
    """Sums total of all savings accounts"""
    if accs is not None:
      return sum([acc.current_amount for acc in accs])
    return sum([acc.current_amount for acc in self.savings_accounts])

  def get_amount_of_savings_accounts(self) -> int:
    """Returns the amount of savings account a user has"""
    return len(self.savings_accounts)

  def get_savings_account_by_name(self, name) -> SavingsAccount:
    """Finds a savings account with a given name"""
    for account in self.savings_accounts:
      if account.name == name:
        return account
    return None

  def get_total_expenses(self) -> float:
    """Sums total of all expenses per month"""
    return sum([expense.monthly_amount for expense in self.expenses])

  def get_income_buffer(self) -> float:
    """Gets amount of months current savings would cover based on expenses"""
    return round(self.get_total_savings(self.user_settings.savings_accounts_for_buffer) / self.get_total_expenses(), 1)
