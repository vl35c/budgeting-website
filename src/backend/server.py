import json

from http.server import BaseHTTPRequestHandler, HTTPServer


TEMP_SPOTLIGHT_DATA = {
  "info": {
    "label": "backend connects",
    "value": "I connected the backend",
    "detail": "It took too long",
    "accent": "#ff7a59",
  }
}


class Handler(BaseHTTPRequestHandler):
  def respond_json(self) -> None:
    self.send_response(200)
    self.send_header("Content-Type", "application/json; charset=utf-8")
    self.end_headers()

  def do_GET(self) -> None:
    if self.path == "/spotlight":
      self.respond_json()
      self.wfile.write(json.dumps(TEMP_SPOTLIGHT_DATA).encode("utf-8"))
      return


server = HTTPServer(("127.0.0.1", 5174), Handler)
print("Serving backend")
server.serve_forever();
