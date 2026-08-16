import json

from http.server import BaseHTTPRequestHandler, HTTPServer

from budget import Budget
from expense import Expense, Frequency
from savings import SavingsAccount
from util import formatGBP, formatPlural


class Handler(BaseHTTPRequestHandler):
  def respond_json(self, json_obj) -> None:
    self.send_response(200)
    self.send_header("Content-Type", "application/json; charset=utf-8")
    self.end_headers()
    self.wfile.write(json.dumps(json_obj).encode("utf-8"))

  def respond_502(self) -> None:
    """502 Bad Gateway"""
    self.send_response(502)

  def __do_GET_budget(self, path: str) -> None:
    """Handle endpoint calls relating to budget"""
    if path == "/savings-accounts":
      self.respond_json(budget.savings_to_web_payload())
      return

  def do_GET(self) -> None:
    """Handle endpoint calls"""
    if self.path.startswith("/budget"):
      self.__do_GET_budget(self.path.removeprefix("/budget"))
      return

    if self.path.startswith("/spotlight/"):
      spotlight = self.path.removeprefix("/spotlight/")

      if spotlight not in TEMP_SPOTLIGHT_DATA:
        self.respond_502()
        return

      self.respond_json(TEMP_SPOTLIGHT_DATA[spotlight])
      return



server = HTTPServer(("127.0.0.1", 5174), Handler)
print("Serving backend")

budget = Budget(
  income=2500.00,
  savings_accounts=[
    SavingsAccount(name="Chase", current_amount=5000.00, interest_rate=3),
    SavingsAccount(name="Emergency", current_amount=2500.00, interest_rate=1.5)
  ],
  expenses=[
    Expense(name="Rent", amount=700.00, frequency=Frequency.MONTHLY),
    Expense(name="Car", amount=300.00, frequency=Frequency.MONTHLY),
    Expense(name="Insurance", amount=70.00, frequency=Frequency.MONTHLY),
    Expense(name="Shopping", amount=100.00, frequency=Frequency.WEEKLY),
    Expense(name="Lunch", amount=5.00, frequency=Frequency.WEEKDAY),
  ]
)

TEMP_SPOTLIGHT_DATA = {
  "savings": {
    "label": "total savings",
    "value": formatGBP(budget.get_total_savings()),
    "detail": f"In {formatPlural(budget.get_amount_of_savings_accounts(), 'account', 'accounts')}",
  },
  "buffer": {
    "label": "income buffer",
    "value": f"{budget.get_income_buffer()} months",
    "detail": "Equivalent of income for period",
  },
  "income": {
    "label": "monthly income",
    "value": formatGBP(budget.income),
    "detail": "",
  },
}

server.serve_forever();
