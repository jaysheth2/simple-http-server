import socket
import threading

def start_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen()
        print(f"Server listening on port {port}")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f'Connected by {addr}')
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

def main():
    ports = [30000, 30010, 30020, 30030, 30040, 30050]
    threads = []

    for port in ports:
        thread = threading.Thread(target=start_server, args=(port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()