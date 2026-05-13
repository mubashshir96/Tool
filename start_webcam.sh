#!/bin/bash
echo "[+] Starting Flask webcam server on port 5000"
python3 webcam_server.py &
PYTHON_PID=$!
sleep 2

echo "[+] Starting Cloudflare tunnel for HTTP"
cloudflared tunnel --url http://localhost:5000 &
CLOUD_PID=$!

echo "[*] Press Ctrl+C to stop both services"
trap "kill $PYTHON_PID $CLOUD_PID 2>/dev/null; exit" INT
wait
