import http.server
import socketserver
import threading

def start_server(port):
  """Starts an HTTP server on the specified port."""
  Handler = http.server.SimpleHTTPRequestHandler
  with socketserver.TCPServer(("", port), Handler) as httpd:
      print("serving at port", port)
      httpd.serve_forever()

# List of ports to start servers on
ports = [30000, 30010, 30020, 30030, 30040, 30050]

# Start servers in separate threads
threads = []
for port in ports:
  thread = threading.Thread(target=start_server, args=(port,))
  threads.append(thread)
  thread.start()

# Keep the main thread alive (optional)
for thread in threads:
  thread.join()
