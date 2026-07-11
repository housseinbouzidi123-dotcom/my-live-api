from http.server import BaseHTTPRequestHandler
import json
import requests
import re

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # التوكن الجديد الطويل جداً الذي أرسلته كقيمة احتياطية في حال الفشل
        new_token = "rX8C4v9Xhu-VYNPe_C3Z7hQX-PIsVMdNfXv8iKjBxmtxAXNQ5RVPII3K51kBJCHG1SKbDoPt8ZcBr1rVyMes8-4gWyaRgwO_8EE7NeBugIWE6e6ikvM1ltVEUKEjUR6hJrwu-6y8tiaHhFOW4LzTMrALE5H5Yp1DiKGb_Jk1FopX6Rs98VVSDtZPPR9dM6PUnkORZv4a21kBJza0COdrah1Op4Ph_MnNGXLUhVkqmgd8eQO58b7zTKV4XNiLyoYdhJXjBKwoI7H3LfFf2LDExfQOW_ruoBKrK6G_WEKdg_Bqp7D0x9BvB2Z12HgBke2LFVtD6rPlGP8JXaQ56w4pz-iL1mm08wuj3zA-QmH2Gdi7uwJoLDqsAbpBjIs-b3rzzgi3WG4G331F17f0mXkNVLtvVpZmLmXZ5048CyplD9Tg2KgL9ebTcXRRU3WDXCHGoxyfqTmT8y6LvAGfSbckml-Mu_YJrCblu7xqCvJsBv1HHAQoaw2AUVdcHodZCmjpi9t40k1Zx6ENmEylDV1rNISHYx2hYqjwE0RXX1lcMBnGPYao22z6qhErZ8xzS4sm6NRd21ZBGHohGw20KAoDHZbxXMIwjTaNSOUlcu5QY2Aydf00ZeY-CZPjBuBmOHiXedhdxphdchxk6CCUC596yRIfU27OYlpIdePQKEosgoYOkwzZkof7Q9GzSFsXF-w0XgFKYOS4T8CLXjH75Zgf9acWtcaueJ57gfIHkF1BBYM"
        
        # الرابط الرئيسي المصطاد الذي يتغير منه التوكن
        source_url = "http://31.59.212.11:8790/auth/قيمة_الرابط_المصطاد" 
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
            "Accept": "*/*"
        }
        
        try:
            response = requests.get(source_url, headers=headers, timeout=4)
            # دالة البحث عن التوكن الجديد في الرابط المحول أو النص
            token_match = re.search(r'auth/([a-zA-Z0-9._-]+)', response.url)
            if token_match:
                new_token = token_match.group(1)
            else:
                token_match_text = re.search(r'auth/([a-zA-Z0-9._-]+)', response.text)
                if token_match_text:
                    new_token = token_match_text.group(1)
        except Exception as e:
            pass

        # بناء روابط القنوات بالتوكن الجديد والمحدث تلقائياً
        streams = {
            "max1_fhd": f"http://31.59.212.11:8790/auth/{new_token}",
            # يمكنك لاحقاً إضافة بقية القنوات مثل max2_fhd و bein1_fhd بنفس الطريقة هنا بشرط تغيير أرقام المنافذ أو المسارات حسب التطبيق الأصلي
        }

        # إرسال الاستجابة بنجاح
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(streams).encode('utf-8'))
        return
