from savings import SavingsAccount


class UserSettings:
  def __init__(self):
    self.savings_accounts_for_buffer: list[SavingsAccount] = []
