import json

from http.server import BaseHTTPRequestHandler, HTTPServer


TEMP_SPOTLIGHT_DATA = {
  "info": {
    "label": "backend connects",
    "value": "I connected the backend",
    "detail": "It took too long",
    "accent": "#ff7a59",
  },
  "savings": {
    "label": "total savings",
    "value": "£7500",
    "detail": "Between 3 Accounts",
    "accent": "#ffb347",
  },
  "buffer": {
    "label": "income buffer",
    "value": "3.5 months",
    "detail": "Equivalent of income for period",
    "accent": "#7ad3ff",
  },
}


class Handler(BaseHTTPRequestHandler):
  def respond_json(self) -> None:
    self.send_response(200)
    self.send_header("Content-Type", "application/json; charset=utf-8")
    self.end_headers()

  def respond_502(self) -> None:
    self.send_response(502)

  def do_GET(self) -> None:
    if self.path.startswith("/spotlight/"):
      spotlight = self.path.removeprefix("/spotlight/")

      if spotlight not in TEMP_SPOTLIGHT_DATA:
        self.respond_502()
        return

      self.respond_json()
      self.wfile.write(json.dumps(TEMP_SPOTLIGHT_DATA[spotlight]).encode("utf-8"))
      return


server = HTTPServer(("127.0.0.1", 5174), Handler)
print("Serving backend")
server.serve_forever();
