#!/bin/bash
echo "[+] Starting PHP file server on port 8000"
php -S 0.0.0.0:8000 &
PHP_PID=$!
sleep 2

echo "[+] Starting Cloudflare tunnel for HTTP"
cloudflared tunnel --url http://localhost:8000 &
CLOUD_PID=$!

echo "[*] Press Ctrl+C to stop both services"
trap "kill $PHP_PID $CLOUD_PID 2>/dev/null; exit" INT
wait
