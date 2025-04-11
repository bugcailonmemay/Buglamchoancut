import threading
import base64
import os
import time
import re
import json
import random
import requests
import socket
import sys
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from faker import Faker
from requests import session
from colorama import Fore, Style
import pystyle
def check_connection():
    try:
        response = requests.get("https://www.google.com.vn", timeout=3)        
    except (requests.exceptions.ReadTimeout, requests.ConnectionError):
        print("Vui lòng kiểm tra kết nối mạng !!!")
        sys.exit()
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"Lỗi: {str(e)}")
check_connection()   
# Tạo hoặc đọc khóa mã hóa bằng base64
secret_key = base64.urlsafe_b64encode(os.urandom(32))

# Mã hóa và giải mã dữ liệu bằng base64
def encrypt_data(data):
    return base64.b64encode(data.encode()).decode()

def decrypt_data(encrypted_data):
    return base64.b64decode(encrypted_data.encode()).decode()

def bes4(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            version_tag = soup.find('span', id='version')
            maintenance_tag = soup.find('span', id='maintenance')
            version = version_tag.text.strip() if version_tag else None
            maintenance = maintenance_tag.text.strip() if maintenance_tag else None
            return version, maintenance
    except requests.RequestException:
        return None, None
    return None, None

def checkver():
    url = 'https://webkeyduykhanh.blogspot.com/2025/02/thong-tin-phien-ban-cong-cu-body-font_31.html?m=1'
    version, maintenance = bes4(url)
    if maintenance == 'on':
        sys.exit()
    return version

current_version = checkver()
if current_version:
    print(f"[</>] Phiên bản hiện tại: {current_version}")
else:
    print("Không thể lấy thông tin phiên bản hoặc tool đang được bảo trì.")
    sys.exit()

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = f"""
██████╗░██╗░░░██╗████████╗░█████╗░░█████╗░██╗░░░░░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██████╔╝╚██╗░██╔╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
██╔══██╗░╚████╔╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░██║░░╚██╔╝░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝

TOOL BY: DUY KHÁNH             PHIÊN BẢN : 1.0
════════════════════════════════════════════════  
[</>] BOX ZALO : https://zalo.me/g/nguadz335
[</>] KÊNH YOUTUBE : REVIEWTOOL247NDK
[</>] ADMIN TOOL : DUYKHANH
❤ CHÀO MỪNG BẠN ĐÃ ĐẾN VỚI TOOL ❤
════════════════════════════════════════════════  
"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.000001)

def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        ip_address = ip_data['ip']
        return ip_address
    except Exception as e:
        print(f"Lỗi khi lấy địa chỉ IP : {e}")
        return None

def display_ip_address(ip_address):
    if ip_address:
        banner()
        print(f"[</>] Địa chỉ IP : {ip_address}")
    else:
        print("BẠN BUG MỘT PHÁT NỮA DÍNH BOTNET NGAY NHÉ !!!")

def luu_thong_tin_ip(ip, key, expiration_date):
    data = {ip: {'key': key, 'expiration_date': expiration_date.isoformat()}}
    encrypted_data = encrypt_data(json.dumps(data))

    with open('ip_key.json', 'w') as file:
        file.write(encrypted_data)

def tai_thong_tin_ip():
    try:
        with open('ip_key.json', 'r') as file:
            encrypted_data = file.read()
        data = json.loads(decrypt_data(encrypted_data))
        return data
    except FileNotFoundError:
        return None

def kiem_tra_ip(ip):
    data = tai_thong_tin_ip()
    if data and ip in data:
        expiration_date = datetime.fromisoformat(data[ip]['expiration_date'])
        if expiration_date > datetime.now():
            return data[ip]['key']
    return None

def generate_key_and_url(ip_address):
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
    key = f'NDK{key1}{ip_numbers}'
    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'https://www.webkey.x10.mx/?ma={key}'   
    return url, key, expiration_date

def da_qua_gio_moi():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    return now >= midnight

def get_shortened_link_phu(url):
    """
    Hàm để rút gọn URL bằng một dịch vụ API.
    """
    try:
        token = "6648c8f016f35d42cd052655"  # Thay bằng API Token Của Bạn
        api_url = f"https://link4m.co/api-shorten/v2?api={token}&url={url}"

        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"status": "error", "message": "Không thể kết nối đến dịch vụ rút gọn URL."}
    except Exception as e:
        return {"status": "error", "message": f"Lỗi khi rút gọn URL: {e}"}

def main():
    ip_address = get_ip_address()
    display_ip_address(ip_address)

    if ip_address:
        existing_key = kiem_tra_ip(ip_address)
        if existing_key:
            print(f"[</>] Tool còn hạn, mời bạn dùng tool...")
            time.sleep(2)
        else:
            if da_qua_gio_moi():
                print("[</>] Quá giờ sử dụng tool !!!")
                return

            url, key, expiration_date = generate_key_and_url(ip_address)

            with ThreadPoolExecutor(max_workers=2) as executor:
                print("[</>] Nhập 1 Để Lấy Key ( Free )")

                while True:
                    try:
                        choice = input("[</>] Nhập lựa chọn: ")
                        print("════════════════════════════════════════════════")                                          
                        if choice == "1":         	
                            yeumoney_future = executor.submit(get_shortened_link_phu, url)
                            yeumoney_data = yeumoney_future.result()
                            if yeumoney_data and yeumoney_data.get('status') == "error":
                                print(yeumoney_data.get('message'))
                                return
                            else:
                                link_key_yeumoney = yeumoney_data.get('shortenedUrl')
                                print('[</>] Link Để Vượt Key Là :', link_key_yeumoney)

                            while True:
                                keynhap = input('[</>] Key Đã Vượt Là : ')
                                if keynhap == key:
                                    print('[</>] Key Đúng Mời Bạn Dùng Tool.....')                                    
                                    sleep(2)
                                    luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                                    return
                                else:
                                    print('[</>] Key Sai Vui Lòng Vượt Lại Link :', link_key_yeumoney)
                    except ValueError:
                        print("Vui lòng nhập số hợp lệ !!!")
                    except KeyboardInterrupt:
                        print("[</>] Cảm ơn bạn đã dùng Tool !!!")
                        sys.exit()
                        

if __name__ == '__main__':
    main()
    

from pystyle import Colors, Colorate
from rich.console import Console
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
import requests,os, random
from time import sleep
list_clone = []
list_img = []
dem = 0
stt = 0
stt2 = 0
# =========================== [ CLASS + FUNCTION TOOL ] ===========================
class API_PRO5_BYREVIEWTOOL:
    def banner(self):
        os.system('title TOOL REG PAGR PRO5 + UP AVT | ĐA LUỒNG')
        os.system("cls" if os.name == "nt" else "clear")
        banner =(""" 
██████╗░██╗░░░██╗████████╗░█████╗░░█████╗░██╗░░░░░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██████╔╝╚██╗░██╔╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
██╔══██╗░╚████╔╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░██║░░╚██╔╝░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝

TOOL BY: DUY KHÁNH             PHIÊN BẢN : 1.0
════════════════════════════════════════════════  
[</>] BOX ZALO : https://zalo.me/g/nguadz335
[</>] KÊNH YOUTUBE : REVIEWTOOL247NDK
[</>] ADMIN TOOL : DUYKHANH
❤ CHÀO MỪNG BẠN ĐÃ ĐẾN VỚI TOOL ❤
════════════════════════════════════════════════  
[</>] GIỚI HẠN THIẾT BỊ : 1 🚦
[</>] NGƯỜI MUA : USER.....
[</>] KEY : NDK*********
════════════════════════════════════════════════  
                  [THÔNG BÁO]
>>>>TOOL ĐANG TRONG QUÁ TRÌNH PHÁT TRIỂN THÊM<<<<     
════════════════════════════════════════════════
""")
        print(banner)
    def rvtool_delay_tool(self, p):
       
        while(p>1):
            p=p-1
            print(f'[REVIEWTOOL] [|][LO......][{p}]','     ',end='\r');sleep(1/6)
            print(f'[REVIEWTOOL] [/][LOA.....][{p}]','     ',end='\r');sleep(1/6)
            print(f'[REVIEWTOOL] [-][LOAD....][{p}]','     ',end='\r');sleep(1/6)
            print(f'[REVIEWTOOL] [+][LOADI...][{p}]','     ',end='\r');sleep(1/6)
            print(f'[REVIEWTOOL] [\][LOADIN..][{p}]','     ',end='\r');sleep(1/6)
            print(f'[REVIEWTOOL] [|][LOADING.][{p}]','     ',end='\r');sleep(1/6)
    def getthongtinfacebook(self, cookie: str):
        
        headers_get = {'authority': 'www.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36','viewport-width': '1184','cookie': cookie}
        try:
            print(f'Đang Tiến Hành Check Live', end="\r")
            url_profile = requests.get('https://www.facebook.com/me', headers = headers_get).url
            get_dulieu_profile = requests.get(url = url_profile, headers = headers_get).text
        except:
            return False
        try:
            uid_get = cookie.split('c_user=')[1].split(';')[0]
            fb_dtsg_get = get_dulieu_profile.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
            jazoest_get = get_dulieu_profile.split('{"name":"jazoest","value":"')[1].split('"},')[0]
            name_get = get_dulieu_profile.split('<title>')[1].split('</title>')[0]
            return name_get,uid_get,fb_dtsg_get,jazoest_get
        except:
            try:
                uid_get = cookie.split('c_user=')[1].split(';')[0]
                fb_dtsg_get = get_dulieu_profile.split(',"f":"')[1].split('","l":null}')[0]
                jazoest_get = get_dulieu_profile.split('&jazoest=')[1].split('","e":"')[0]
                name_get = get_dulieu_profile.split('<title>')[1].split('</title>')[0]
                return name_get,uid_get,fb_dtsg_get,jazoest_get
            except:
                return False    
    def RegPage(self, cookie, name, uid, fb_dtsg, jazoest):
        
        namepage = requests.get('https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/male?count=2').json()['data'][0]['name']
        global dem
        headers_reg = {'authority': 'www.facebook.com','accept': '*/*','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','origin': 'https://www.facebook.com','referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','viewport-width': '979','x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation','x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY','cookie': cookie}
        data_reg = {'av': uid,'__user': uid,'__a': '1','__dyn': '7AzHxq1mxu1syUbFuC0BVU98nwgU29zEdEc8co5S3O2S7o11Ue8hw6vwb-q7oc81xoswIwuo886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3qxWm2Sq2-azo2NwkQ0z8c84K2e3u362-2B0oobo','__csr': 'gP4ZAN2d-hbbRmLObkZO8LvRcXWVvth9d9GGXKSiLCqqr9qEzGTozAXiCgyBhbHrRG8VkQm8GFAfy94bJ7xeufz8jK8yGVVEgx-7oiwxypqCwgF88rzKV8y2O4ocUak4UpDxu3x1K4opAUrwGx63J0Lw-wa90eG18wkE7y14w4hw6Bw2-o069W00CSE0PW06aU02Z3wjU6i0btw3TE1wE5u','__req': 't','__hs': '19296.HYP:comet_pkg.2.1.0.2.1','dpr': '1','__ccg': 'EXCELLENT','__rev': '1006496476','__s': '1gapab:y4xv3f:2hb4os','__hsi': '7160573037096492689','__comet_req': '15','fb_dtsg': fb_dtsg,'jazoest': jazoest,'lsd': 'ZM7FAk6cuRcUp3imwqvHTY','__aaid': '800444344545377','__spin_r': '1006496476','__spin_b': 'trunk','__spin_t': '1667200829','fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation','variables': '{"input":{"bio":"reg auto by duykhanh","categories":["181475575221097"],"creation_source":"comet","name":"'+namepage+'","page_referrer":"launch_point","actor_id":"'+uid+'","client_mutation_id":"1"}}','server_timestamps': 'true','doc_id': '5903223909690825',}
        try:
            idpage = requests.post('https://www.facebook.com/api/graphql/', headers=headers_reg, data=data_reg, timeout=20).json()['data']['additional_profile_plus_create']['additional_profile']['id']
            dem+=1
            print(f'{dem} | SUCCESS | NAME FB: {name} | UID PRO5: {idpage} | NAME PRO5: {namepage}')
            return idpage
        except:
            print('[</>] Reg Thất Bại Có Vẻ Acc Của Bạn Đã Bị Block!!')
            return False
# =========================== [ START TOOL ] ===========================
duykhanh = API_PRO5_BYREVIEWTOOL()
duykhanh.banner()
print('[ENTER - ĐỂ DỪNG NHẬP]')
while True:
    stt+=1
    cookie_fb = input(f'[</>] VUI LÒNG NHẬP COOKIE THỨ [{stt}]:')
    if cookie_fb == '':
        break
    checklive = duykhanh.getthongtinfacebook(cookie_fb)
    if checklive != False:
        print('[</>] Name Facebook:  '+checklive[0])
        list_clone.append(f'{cookie_fb}|{checklive[0]}|{checklive[1]}|{checklive[2]}|{checklive[3]}')
        print('─'*50)
    else:
        stt-1
        print('Cookie '+cookie_fb.split('c_user=')[1].split(';')[0]+', Die Or Out Vui Lòng Kiểm Tra Lại!!')
# Tiến Hành Nhập Setting Reg Page
print('─'*50)
slpage = int(input('[</>] BẠN MUỐN TẠO BAO NHIÊU PAGE THÌ DỪNG TOOL: '))
print('─'*50)
delay = int(input('[</>] VUI LÒNG NHẬP DELAY REG PAGE: '))
print('─'*50)
# Tiến Hành Chạy Tool
duykhanh.banner()
while True:
    for dulieuclone in list_clone:
        idpage = duykhanh.RegPage(str(dulieuclone).split('|')[0], str(dulieuclone).split('|')[1], str(dulieuclone).split('|')[2], str(dulieuclone).split('|')[3], str(dulieuclone).split('|')[4])        
        duykhanh.rvtool_delay_tool(delay)
        if dem == slpage:
            input(f'[</>] Done {dem}, Page </> ENTER ĐỂ EXIT')
            exit()