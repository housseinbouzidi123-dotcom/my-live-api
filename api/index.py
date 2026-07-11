from http.server import BaseHTTPRequestHandler
import urllib.parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # استخراج التوكن
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        token = query.get('token', [None])[0]

        if not token:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Token missing")
            return

        target_url = f"http://31.59.212.10:8790/auth/{token}"
        
        # محاكاة طلب التطبيق الأصلي
        headers = {
            "User-Agent": "com.rayan.iqrebrand/43 (Linux; U; Android 9; en_US; V2217A; Build/PQ3A.190605.06171433; Cronet/99.0.4844.35)",
            "Accept-Encoding": "identity"
        }

        try:
            # سحب البيانات وإعادة بثها (Proxy Streaming)
            response = requests.get(target_url, headers=headers, stream=True, timeout=15)
            self.send_response(response.status_code)
            
            # تمرير الهيدرز الضرورية للمشغل
            for key, value in response.headers.items():
                if key.lower() not in ['content-encoding', 'transfer-encoding']:
                    self.send_header(key, value)
            self.end_headers()
            
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    self.wfile.write(chunk)
        except Exception as e:
            self.send_response(502)
            self.end_headers()
            self.wfile.write(str(e).encode())
