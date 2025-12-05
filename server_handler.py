from http.server import SimpleHTTPRequestHandler as handler
from socketserver import TCPServer as server
from sys import exit


PORT = 8080

with server(("", PORT), handler) as httpd:
    print(f"Serving at port {PORT}")
    # Start the server and keep it running until you stop the script
    httpd.serve_forever()

def stop_execution(user_input: str) -> None:
    if (user_input.lower == "q" or user_input.lower == "quit" or user_input.lower =="exit"):
        exit()
    else:
        return

while (True):
    stop_execution(input())
