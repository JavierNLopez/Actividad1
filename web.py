from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(self.get_response().encode("utf-8"))

    def get_response(self):
        parsed_url = self.url()
        path = parsed_url.path
        query = self.query_data()
        
        if path.startswith("/proyecto/"):
            proyecto = path.split("/")[-1]
            autor = query.get("autor", "desconocido")
            return f"<h1>Proyecto: {proyecto} Autor: {autor}</h1>"
        
        return "<h1>Ruta no valida</h1>"


if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()
