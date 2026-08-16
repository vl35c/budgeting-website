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