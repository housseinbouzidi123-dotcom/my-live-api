from http.server import BaseHTTPRequestHandler
import json
import requests
import re

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. جلب التوكن الجديد (تأكد من تعديل الرابط والـ User-Agent أدناه بما يناسب التطبيق الأصلي)
        source_url = "http://217.60.15.181:8080/قيمة_الرابط_المصطاد" 
        headers = {
            "User-Agent": "ضع هنا الـ User-Agent المصطاد من التطبيق",
            "Accept": "*/*"
        }
        
        try:
            response = requests.get(source_url, headers=headers, timeout=5)
            token_match = re.search(r'token=([a-zA-Z0-9._-]+)', response.text)
            new_token = token_match.group(1) if token_match else "yXzbaHc.fyaXy..."
        except:
            new_token = "yXzbaHc.fyaXy..." # توكن احتياطي في حال الفشل

        # 2. بناء قائمة كافة قنوات البث بالتوكن الجديد المتجدد تلقائياً
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
            "max4_fhd": "http://195.182.16.54:8080/live/54:3a:d6:35:30:f0/4446898654/460870.ts",
            "max1_hd": "http://195.182.16.54:8080/live/54:3a:d6:35:30:f0/4446898654/460862.ts",
            "max2_hd": "http://195.182.16.45:8080/live/omar777/01103978590/460865.ts",
            "max3_hd": "http://195.182.16.48:8080/live/54:3a:d6:35:30:f0/4446898654/460868.ts",
            "max4_hd": "http://195.182.16.53:8080/live/54:3a:d6:35:30:f0/4446898654/460871.ts",
            "max1_sd": "http://195.182.16.45:8080/live/omar77777/01103978590/460862.ts",
            "max2_sd": "http://195.182.16.45:8080/live/omar777/01103978590/460866.ts",
            "max3_sd": "http://195.182.16.45:8080/live/omar777/01103978590/460869.ts",
            "max4_sd": "http://195.182.16.45:8080/live/omar777/01103978590/460872.ts"
        }

        # 3. إرسال الاستجابة للووركر بصيغة JSON
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(streams).encode('utf-8'))
        return
