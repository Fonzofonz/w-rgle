import http.server
import socketserver

PORT = 8080

class HelloHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Setze den Antwort-Header
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Schreibe den Inhalt der Webseite
        self.wfile.write(b"Hello, World oder so!")

with socketserver.TCPServer(("", PORT), HelloHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
