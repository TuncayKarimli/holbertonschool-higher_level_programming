#!/usr/bin/python3
"""
A simple HTTP server built using http.server to handle different
endpoints and serve both text and JSON data.
"""
import http.server
import socketserver
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    HTTP Request Handler to manage different API endpoints.
    """

    def do_GET(self):
        """Handle GET requests for specific paths."""
        
        # Route: Root /
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Route: /data (JSON)
        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # Route: /status
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # Route: /info
        elif self.path == '/info':
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('utf-8'))

        # Route: 404 Not Found
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    PORT = 8000
    # Use allow_reuse_address to avoid "Address already in use" errors during testing
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
