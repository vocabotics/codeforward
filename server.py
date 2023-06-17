################################################################################
# File Name: server.py
# Author: vocabotics - Jon Ross
# Twitter: @vocaboticsai
# Github: https://github.com/vocabotics/codeforward
# Date: 18/6/2023
################################################################################


import http.server
import socketserver
import threading

def run_server():
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print(f"serving at port {PORT}")
    httpd.serve_forever()

if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopping server...")
