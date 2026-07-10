from http.server import BaseHTTPRequestHandler
import json
import requests
import re

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. جلب التوكن الجديد من الرابط المصطاد
        source_url = "http://217.60.15.181:8080/قيمة_الرابط_المصطاد" 
        headers = {
            "User-Agent": "ضع هنا الـ User-Agent المصطاد من التطبيق",
            "Accept": "*/*"
        }
        
        try:
            response = requests.get(source_url, headers=headers, timeout=5)
            token_match = re.search(r'token=([a-zA-Z0-9._-]+)', response.text)
            new_token = token_match.group(1) if token_match else "yXzbaHc..."
        except:
            new_token = "yXzbaHc..."

        # 2. بناء مصفوفة الروابط المتجددة
        streams = {
            "bein1_fhd": f"http://217.60.15.181:8080/live///b0:99:d7:15:88:50/3090914536649669/318197.ts?token={new_token}",
            "bein2_fhd": f"http://217.60.15.181:8080/live///b0:99:d7:15:88:50/3090914536649669/318198.ts?token={new_token}",
        }

        # 3. إرسال الاستجابة للووركر
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.end_headers()
        self.wfile.write(json.dumps(streams).encode('utf-8'))
        return