from enum import Enum

from util import formatGBP


class Frequency(Enum):
  MONTHLY = 1
  WEEKLY = 2
  DAILY = 3
  WEEKDAY = 4


class Expense:
  def __init__(self, name: str="", amount: float=0, frequency: Frequency=Frequency.MONTHLY):
    self.name = name
    self.amount = amount
    self.frequency = frequency

  @property
  def monthly_amount(self) -> float:
    if self.frequency == Frequency.MONTHLY:
      return self.amount * 1  # average months in a month :)
    if self.frequency == Frequency.WEEKLY:
      return self.amount * 4.33  # average weeks in a month
    if self.frequency == Frequency.WEEKDAY:
      return self.amount * 22  # average weekdays in a month
    if self.frequency == Frequency.DAILY:
      return self.amount * 30  # average days in a month

  def to_web_payload(self) -> dict:
    """Returns object as json payload"""
    return {
      "name": self.name,
      "amount": formatGBP(self.amount),
      "monthly_amount": formatGBP(self.monthly_amount),
      "frequency": self.frequency.__str__(),
    }
