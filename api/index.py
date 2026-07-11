from http.server import BaseHTTPRequestHandler
import json
import requests
import re

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # توكن افتراضي احتياطي حتى لا ينهار السيرفر أبداً في حال فشل جلب التوكن الديناميكي
        new_token = "yXzbaHc.fyaXy.X.faUdz.ydzzcXfHbU.X.y.FR.ts.e6bded1b8bf057cc3a0b376e0145f8970425b4bf83bcfab782614901bcc624ae.5089.VmlyZ2luIE1lZGlh.MTg1LjE5MS4xMjYuMTI3"
        
        # الرابط المصطاد من تطبيق جلب البث (تأكد لاحقاً من وضع الرابط الصحيح كاملاً هنا)
        source_url = "http://217.60.15.181:8080/live///b0:99:d7:15:88:50/3090914536649669/318197.ts" 
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
            "Accept": "*/*"
        }
        
        try:
            # محاولة جلب التوكن الجديد تلقائياً
            response = requests.get(source_url, headers=headers, timeout=4)
            # إذا كان الرابط يعيد التوجيه إلى رابط يحتوي على التوكن
            final_url = response.url
            token_match = re.search(r'token=([a-zA-Z0-9._-]+)', final_url)
            
            if token_match:
                new_token = token_match.group(1)
            else:
                # محاولة البحث داخل نص الاستجابة نفسه إذا لم يكن في الرابط
                token_match_text = re.search(r'token=([a-zA-Z0-9._-]+)', response.text)
                if token_match_text:
                    new_token = token_match_text.group(1)
        except Exception as e:
            # في حال حدوث أي خطأ في الاتصال، سيستمر السكريبت بالعمل دون الانهيار وسيعتمد التوكن الاحتياطي
            pass

        # بناء قائمة القنوات بالتوكن المتاح
        streams = {
            # ===================== FHD =====================
            "bein1_fhd": f"http://217.60.15.181:8080/live///b0:99:d7:15:88:50/3090914536649669/318197.ts?token={new_token}",
            "bein2_fhd": f"http://217.60.15.181:8080/live///b0:99:d7:15:88:50/3090914536649669/318198.ts?token={new_token}",
            "bein3_fhd": f"http://217.60.15.181:8080/live///b0:99:d7:15:88:50/3090914536649669/318199.ts?token={new_token}",
            "bein4_fhd": f"http://172.110.216.28:2095/live///b0:99:d7:15:88:50/3090914536649669/440580.ts?token={new_token}",
            "bein5_fhd": f"http://217.60.15.181:8080/live///b0:99:d7:15:88:50/3090914536649669/318201.ts?token={new_token}",
            "bein6_fhd": f"http://217.60.15.181:8080/live///b0:99:d7:15:88:50/3090914536649669/318202.ts?token={new_token}",
            "bein7_fhd": f"http://217.60.15.181:8080/live///b0:99:d7:15:88:50/3090914536649669/318203.ts?token={new_token}",
            "bein8_fhd": f"http://217.60.15.181:8080/live///b0:99:d7:15:88:50/3090914536649669/318204.ts?token={new_token}",
            "bein9_fhd": f"http://217.60.15.181:8080/live///b0:99:d7:15:88:50/3090914536649669/318205.ts?token={new_token}",

            # ===================== HD =====================
            "bein1_hd": f"http://172.110.216.28:2095/live///b0:99:d7:15:88:50/3090914536649669/325793.ts?token={new_token}",
            "bein2_hd": f"http://217.60.15.181:8080/live///b0:99:d7:15:88:50/3090914536649669/391095.ts?token={new_token}",
            "bein3_hd": f"http://172.110.216.28:2095/live///b0:99:d7:15:88:50/3090914536649669/325795.ts?token={new_token}",
            "bein4_hd": f"http://172.110.216.28:2095/live///b0:99:d7:15:88:50/3090914536649669/325796.ts?token={new_token}",
            "bein5_hd": f"http://172.110.216.28:2095/live///b0:99:d7:15:88:50/3090914536649669/325797.ts?token={new_token}",
            "bein6_hd": f"http://172.110.216.28:2095/live///b0:99:d7:15:88:50/3090914536649669/325798.ts?token={new_token}",
            "bein7_hd": f"http://172.110.216.28:2095/live///b0:99:d7:15:88:50/3090914536649669/325799.ts?token={new_token}",
            "bein8_hd": f"http://172.110.216.28:2095/live///b0:99:d7:15:88:50/3090914536649669/325800.ts?token={new_token}",
            "bein9_hd": f"http://172.110.216.28:2095/live///b0:99:d7:15:88:50/3090914536649669/325801.ts?token={new_token}",

            # ===================== SD =====================
            "bein1_sd": f"http://217.60.15.141:2095/live///b0:99:d7:15:88:50/3090914536649669/325803.ts?token={new_token}",
            "bein2_sd": f"http://217.60.15.141:2095/live///b0:99:d7:15:88:50/3090914536649669/325804.ts?token={new_token}",
            "bein3_sd": f"http://217.60.15.141:2095/live///b0:99:d7:15:88:50/3090914536649669/325805.ts?token={new_token}",
            "bein4_sd": f"http://217.60.15.141:2095/live///b0:99:d7:15:88:50/3090914536649669/325806.ts?token={new_token}",
            "bein5_sd": f"http://217.60.15.141:2095/live///b0:99:d7:15:88:50/3090914536649669/325807.ts?token={new_token}",
            "bein6_sd": f"http://217.60.15.130:2095/live///b0:99:d7:15:88:50/3090914536649669/325808.ts?token={new_token}",
            "bein7_sd": f"http://217.60.15.141:2095/live///b0:99:d7:15:88:50/3090914536649669/325809.ts?token={new_token}",
            "bein8_sd": f"http://217.60.15.130:2095/live///b0:99:d7:15:88:50/3090914536649669/325810.ts?token={new_token}",
            "bein9_sd": f"http://217.60.15.141:2095/live///b0:99:d7:15:88:50/3090914536649669/325811.ts?token={new_token}",

            # ===================== BeIN MAX الثابتة =====================
            "max1_fhd": "http://195.182.16.45:8080/live/omar777/01103978590/460861.ts",
            "max2_fhd": "http://195.182.16.45:8080/live/omar777/01103978590/460864.ts",
            "max3_fhd": "http://195.182.16.45:8080/live/omar777/01103978590/460867.ts",
            "max4_fhd": "http://195.182.16.54:8080/live/54:3a:d6:35:30:f0/4446898654/460870.ts"
        }

        # إرسال الاستجابة بنجاح لمتصفح الويب أو الووركر
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(streams).encode('utf-8'))
        return
