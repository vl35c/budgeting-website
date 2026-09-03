import json
import requests

from datetime import datetime, timedelta

from tools.env_manager import EnvManager


class Conversion:
  def __init__(self):
    self.data = None
    self.env_manager = EnvManager()

    try:
      with open("src/assets/data/conversion_rates.json", "r") as file:
        try:
          self.data = json.loads(file.read())
          self.__check_meta_date()
        except Exception:
          raise Exception("Unable to read conversion rate json")
    except FileNotFoundError:
      raise Exception("Conversion Data not found")

  def __check_meta_date(self):
    """If data is from before yesterday, it is stale"""
    try:
      date = self.data["meta"]["last_updated_at"]
    except KeyError:
      # if no data is found
      # only update if no data is found
      # let user manually decide if data is stale
      if "data" not in self.data:
        self.__update_data()
        return

    date_obj = datetime.fromisoformat(date).date()
    stale_date = (datetime.now() - timedelta(days=1)).date()
        
    if (date_obj < stale_date):
      self.__update_data()

  def __update_data(self):
    """Calls API to update conversion rate data"""
    key = self.env_manager.get_var("CURRENCY_API")
    url = f"https://api.currencyapi.com/v3/latest?apikey={key}&base_currency=GBP"

    try:
      response = requests.get(url).json()
      print("[CURRENCY API]: Received Response")
    except ConnectionError:
      return  # don't update if no connection
        
    with open("src/assets/data/conversion_rates.json", "w") as file:
      file.write(json.dumps(response, indent=2))

    print("[CURRENCY API]: Updated currency conversion rates")

  def get_currency(self, currency: str) -> dict:
    """Returns all data about a currency"""
    return self.data["data"][currency]

  def convert_currency(self, to_ccy: str) -> float:
    """Returns conversion rate of GBP to target currency"""
    to_value = self.data["data"][to_ccy]["value"]
    return to_value

  def to_web_payload(self, include_meta: bool=False) -> dict:
    """
    Returns data
    include_meta: bool - whether metadata should be included
    """
    if not include_meta:
      return { "currencies": [v for v in self.data["data"].values()] }
    return self.data
