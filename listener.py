#!/usr/bin/env python3
import socket
import sys
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def start_listener(port=4444):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print(f"[+] TCP listener started on port {port}")
    print("[*] Waiting for incoming connection...")

    while True:
        conn, addr = server.accept()
        print(f"[+] Connection from {addr}")
        log_file = os.path.join(LOG_DIR, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        with open(log_file, 'ab') as f:
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                f.write(data)
                sys.stdout.write(data.decode(errors='ignore'))
                sys.stdout.flush()
        print(f"[-] Connection closed. Log saved: {log_file}")

if __name__ == "__main__":
    port = 4444
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    start_listener(port)
