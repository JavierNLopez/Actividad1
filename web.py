from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        path = self.url().path
        contenido = self.get_response()
        
        if contenido is None:
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write("<h1>404 - Pagina no encontrada</h1>".encode("utf-8"))
            
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(contenido.encode("utf-8"))

    def get_response(self):
        path = self.url().path

        if path == "/":
            try:
                with open("home.html", "r", encoding="utf-8") as f:
                    return f.read()
            except FileNotFoundError:
                return f"<h1>Proyecto: {proyecto} Autor: {autor}</h1>"

        return None

if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()
