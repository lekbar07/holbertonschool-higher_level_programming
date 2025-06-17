#!/usr/bin/env python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_response(self, code, content, content_type="text/plain"):
        self.send_response(code)
        self.send_header('Content-type', content_type)
        self.end_headers()
        if isinstance(content, str):
            self.wfile.write(content.encode('utf-8'))
        else:
            self.wfile.write(content)

    def do_GET(self):
        if self.path == "/":
            self._send_response(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self._send_response(200, json.dumps(data), content_type="application/json")
        elif self.path == "/status":
            self._send_response(200, "OK")
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._send_response(200, json.dumps(info), content_type="application/json")
        else:
            self._send_response(404, "Endpoint not found")

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server at http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

