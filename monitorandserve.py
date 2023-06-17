################################################################################
# File Name: monitorandserve.py
# Author: vocabotics - Jon Ross
# Twitter: @vocaboticsai
# Github: https://github.com/vocabotics/codeforward
# Date: 18/6/2023
################################################################################


import os
import time
import http.server
import socketserver
import threading

def concatfiles():
    with open('latestcode.html', 'w') as outfile:
        for filename in os.listdir('.'):
            if filename.endswith(('.txt', '.py', '.css', '.js', '.json')):
                with open(filename) as infile:
                    outfile.write(f'<h2>File: {filename}</h2>\n')
                    outfile.write(f'<p>Modified: {time.ctime(os.path.getmtime(filename))}</p>\n')
                    outfile.write('<hr>\n')
                    outfile.write('<pre>\n')
                    outfile.write(infile.read())
                    outfile.write('</pre>\n')
                    outfile.write('<br><br>\n')

def run_server():
    PORT = 8001
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print(f"serving at port {PORT}")
    httpd.serve_forever()

if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

    try:
        while True:
            concatfiles()  # update latestcode.html
            time.sleep(10)  # wait for 10 seconds
    except KeyboardInterrupt:
        print("Stopping server...")
