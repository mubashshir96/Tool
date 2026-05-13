#!/bin/bash
echo "[+] Starting Cloudflare TCP tunnel on port 4444"
echo "[*] Make sure your Android app connects to the address shown below"
cloudflared tunnel --url tcp://localhost:4444
