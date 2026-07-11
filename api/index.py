from http.server import BaseHTTPRequestHandler
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # الجزء الخاص بالمسار من الرابط (أي ما بعد /auth/)
        path_part = self.path.split("/auth/")[-1]
        target_url = "http://31.59.212.10:8790/auth/" + path_part
        
        # Headers ضرورية جداً لمحاكاة التطبيق الأصلي
        headers = {
            "User-Agent": "com.rayan.iqrebrand/43 (Linux; U; Android 9; en_US; V2217A; Build/PQ3A.190605.06171433; Cronet/99.0.4844.35)",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive"
        }

        try:
            # طلب البث مع تفعيل خاصية Streaming
            response = requests.get(target_url, headers=headers, stream=True, timeout=10)
            
            # إعادة إرسال الرد الأصلي للتطبيق
            self.send_response(response.status_code)
            for key, value in response.headers.items():
                if key.lower() not in ['content-encoding', 'transfer-encoding']:
                    self.send_header(key, value)
            self.end_headers()
            
            # نقل البيانات قطعة قطعة (Chunked Streaming) لضمان عدم توقف البث
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    self.wfile.write(chunk)
                
        except Exception as e:
            # في حالة فشل الاتصال بالسيرفر
            self.send_response(502)
            self.end_headers()
            self.wfile.write(str(e).encode())
