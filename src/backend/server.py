import json

from http.server import BaseHTTPRequestHandler, HTTPServer

from budget import Budget
from expense import Expense, Frequency
from savings import SavingsAccount
from templates.spotlight import SpotlightData
from user_settings import UserSettings
from util import formatGBP, formatPlural


class Handler(BaseHTTPRequestHandler):
  def respond_json(self, *json_objs) -> None:
    """Collates all objects passed in into 1 payload and sends"""
    json_obj = {}
    for obj in json_objs:
      json_obj.update(obj)

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
      self.respond_json(budget.savings_to_web_payload(
        attr=self.args["attr"],
        reverse=(True if (self.args["reverse"]) == "on" else False)  # checkbox passes 'on' or 'null'
      ))
      return

    if path == "/buffer-accounts":
      self.respond_json(
        budget.savings_to_web_payload(attr="name", reverse=False),
        budget.savings_buffer_to_web_payload()
      )
      return

    if path == "/update-buffer-accounts":
      accounts = self.args["accounts"].split(';')[:-1]  # remove last as alway have trailing ;
      budget.update_savings_accounts_for_buffer(accounts)
      self.respond_json()  # blank json to not return 502
      return

  def do_GET(self) -> None:
    """Handle endpoint calls"""
    self.args = None  # ensure always defined on GET, and reset on every call

    # if url in form abc/xyz?arg=value
    # remove args and parse url, keep args for later use
    if len(items := self.path.split("?")) == 2:
      self.path, self.args = items
      self.parse_args()

    if self.path.startswith("/budget"):
      self.__do_GET_budget(self.path.removeprefix("/budget"))
      return

    if self.path.startswith("/spotlight/"):
      spotlight = self.path.removeprefix("/spotlight/")

      if not spotlight_data.check_data(spotlight):
        self.respond_502()
        return

      self.respond_json(spotlight_data.get_data(spotlight))
      return

  def parse_args(self) -> None:
    """Takes args from format a=b,c=d -> {a: "b", c: "d"}"""
    arg_map = {}
    args = self.args.split(",")

    for arg in args:
      key, value = arg.split("=")
      arg_map[key] = value

    self.args = arg_map
    print(self.args)


server = HTTPServer(("127.0.0.1", 5174), Handler)
print("Serving backend")

budget = Budget(
  income=2500.00,
  savings_accounts=[
    SavingsAccount(name="Chase", current_amount=5_000.00, interest_rate=3),
    SavingsAccount(name="Emergency", current_amount=2_500.00, interest_rate=1.5),
    SavingsAccount(name="House", current_amount=20_000.00, interest_rate=4.5),
    SavingsAccount(name="ISA", current_amount=12_000, interest_rate=5.5),
  ],
  expenses=[
    Expense(name="Rent", amount=700.00, frequency=Frequency.MONTHLY),
    Expense(name="Car", amount=300.00, frequency=Frequency.MONTHLY),
    Expense(name="Insurance", amount=70.00, frequency=Frequency.MONTHLY),
    Expense(name="Shopping", amount=100.00, frequency=Frequency.WEEKLY),
    Expense(name="Lunch", amount=5.00, frequency=Frequency.WEEKDAY),
  ],
  user_settings=UserSettings(),
)

budget.init_user_settings()

spotlight_data = SpotlightData(budget=budget)

server.serve_forever();
