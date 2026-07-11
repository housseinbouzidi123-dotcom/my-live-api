from http.server import BaseHTTPRequestHandler
import urllib.parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # استخراج التوكن من الرابط كمتغير ?token=...
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        token = query.get('token', [None])[0]

        if not token:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Token missing")
            return

        # الرابط الأصلي للسيرفر مع التوكن
        target_url = f"http://31.59.212.10:8790/auth/{token}"
        
        # التوجيه المباشر للمشغل
        self.send_response(302)
        self.send_header('Location', target_url)
        self.end_headers()
