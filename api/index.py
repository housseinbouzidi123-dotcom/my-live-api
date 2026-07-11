from http.server import BaseHTTPRequestHandler
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # قائمة القنوات: هنا تضع مسارات البث الخاصة بك
        # يجب أن تضع الرابط الذي يعمل حالياً للقناة
        channels = {
            "max1": "http://31.59.212.10:8790/auth/رابط_التوكن_الجديد_للقناة_الاولى",
            "bein1": "http://31.59.212.10:8790/auth/رابط_التوكن_الجديد_للقناة_الثانية"
        }
        
        # تحليل الرابط لاستخراج اسم القناة
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        channel_name = query.get('ch', ['max1'])[0]
        
        target_url = channels.get(channel_name)

        if target_url:
            # توجيه المشغل الخارجي مباشرة إلى رابط البث (302 Redirect)
            self.send_response(302)
            self.send_header('Location', target_url)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Channel not found")
