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
    

#/c/ea991b37-e128-4c96-bfa6-54b7e9abf68c
import hashlib
import random
import requests
import time
from datetime import datetime
import json
import sys
import urllib3
def check_connection():
    try:
        response = requests.get("https://www.google.com.vn", timeout=3)        
    except (requests.exceptions.ReadTimeout, requests.ConnectionError):
        print("Vui lòng kiểm tra kết nối mạng !!!")
        sys.exit()
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"Lỗi: {str(e)}")
check_connection()   
mo_ngoac = "["
dong_ngoac = "]"
mo_ngoac_do = "["
mo_ngoac_xl = "["
mo_ngoac_cam = "["
mo_ngoac_xd = "["
mo_ngoac_hong = "["

# Màu
xanhchuoi = "\x1b[1;38;2;173;255;47m"  # xanh chuối
xanhla = "\033[1;32m"  # xanh lá
do = "\033[1;31m"  # đỏ
trang = "\x1b[1;38;2;233;233;233m"  # trắng đậm
resetmau = "\033[0m\33[1m"  # đặt lại màu
xanhduong = "\x1b[1;38;2;135;206;250m"  # xanh d nhạt
hong = "\x1b[1;38;2;255;182;193m"  # hồng nhạt
cam = "\x1b[1;38;2;255;165;0m"  # cam

# Thanh gạch
que = ''.join(['─'] * 50)
thanh = f"{xanhduong}{que}{resetmau}"
gach = ''.join(['═'] * 20)

# Vô hiệu hóa các cảnh báo InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Cấu hình API và Key
app = {
    'api_key': '882a8490361da98702bf97a021ddc14d',
    'secret': '62f8ce9f74b12f84c123cc23437a4a32',
    'key': ['ChanHungCoder_KeyRegFBVIP_9999', 'DCHVIPKEYREG']
}

email_prefix = [
    'gmail.com',
    'hotmail.com',
    'yahoo.com',
    'outlook.com',
]

# Hàm tạo tài khoản
def create_account():
    # Tạo ngày sinh ngẫu nhiên
    random_birth_day = datetime.strftime(datetime.fromtimestamp(random.randint(
        int(time.mktime(datetime.strptime('1980-01-01', '%Y-%m-%d').timetuple())),
        int(time.mktime(datetime.strptime('1995-12-30', '%Y-%m-%d').timetuple()))
    )), '%Y-%m-%d')

    # Danh sách tên
    names = {
        'first': ['JAMES', 'JOHN', 'ROBERT', 'MICHAEL', 'WILLIAM', 'DAVID'],
        'last': ['SMITH', 'JOHNSON', 'WILLIAMS', 'BROWN', 'JONES', 'MILLER'],
        'mid': ['Alexander', 'Anthony', 'Charles', 'Dash', 'David', 'Edward']
    }

    # Tạo tên ngẫu nhiên
    random_first_name = random.choice(names['first'])
    random_name = f"{random.choice(names['mid'])} {random.choice(names['last'])}"
    password = f'RVTOOL{random.randint(0, 9999999)}?#@'
    full_name = f"{random_first_name} {random_name}"
    md5_time = hashlib.md5(str(time.time()).encode()).hexdigest()

    # Tạo hash và email ngẫu nhiên
    hash_ = f"{md5_time[0:8]}-{md5_time[8:12]}-{md5_time[12:16]}-{md5_time[16:20]}-{md5_time[20:32]}"
    email_rand = f"{full_name.replace(' ', '').lower()}{hashlib.md5((str(time.time()) + datetime.strftime(datetime.now(), '%Y%m%d')).encode()).hexdigest()[0:6]}@{random.choice(email_prefix)}"
    gender = 'M' if random.randint(0, 10) > 5 else 'F'

    # Tạo yêu cầu đăng ký
    req = {
        'api_key': app['api_key'],
        'attempt_login': True,
        'birthday': random_birth_day,
        'client_country_code': 'EN',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': random_first_name,
        'format': 'json',
        'gender': gender,
        'lastname': random_name,
        'email': email_rand,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': hash_,
        'return_multiple_errors': True
    }

    sig = ''.join([f'{k}={v}' for k, v in sorted(req.items())])
    ensig = hashlib.md5((sig + app['secret']).encode()).hexdigest()
    req['sig'] = ensig

    api = 'https://b-api.facebook.com/method/user.register'

    def _call(url='', params=None, post=True):
        headers = {
            'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'
        }
        if post:
            response = requests.post(url, data=params, headers=headers, verify=False)
        else:
            response = requests.get(url, params=params, headers=headers, verify=False)
        return response.text

    reg = _call(api, req)
    reg_json = json.loads(reg)
    uid = reg_json.get('session_info', {}).get('uid')
    access_token = reg_json.get('session_info', {}).get('access_token')

    # Nếu có lỗi, sẽ có các khóa error_code và error_msg trong JSON
    error_code = reg_json.get('error_code')
    error_msg = reg_json.get('error_msg')

    if uid is not None and access_token is not None:
        data_to_save = f"{random_birth_day}:{full_name}:{email_rand}:{password}:{uid}:{access_token}"
        
        with open(file_name, "a") as file:
            file.write(data_to_save + "\n")
        # In thông tin ra màn hình
        print("Birthday:", random_birth_day)
        print("Fullname:", full_name)
        print("Email:", email_rand)
        print("Password:", password)
        print("UID:", uid)
        print("Token:", access_token)
        print(thanh)
    else:
        # Nếu có lỗi, in mã lỗi và thông báo lỗi
        if error_code and error_msg:
            print(f"Error Code: {error_code}")
            print(f"Error Message: {error_msg}")
        else:
            print(f"{do}Unknown error occurred.{resetmau}")
        print(f"{mo_ngoac_cam}×{dong_ngoac} Không Thể Lưu Thông Tin. Vui Lòng Đợi Reg Lại!")

while True:
    try:
        account_count = int(input(f"{mo_ngoac}*{dong_ngoac} Nhập Số Lượng Acc Muốn Reg: "))
        if account_count > 0:
            break
        else:
            print(f"{mo_ngoac_do}!{dong_ngoac} Số Lượng Acc Phải Lớn Hơn 0. Vui Lòng Nhập lại!")
    except ValueError:
        print(f"{mo_ngoac_do}!{dong_ngoac} Nội Dung Nhập Không Hợp Lệ!")

while True:
    file_name = input(f"{mo_ngoac}*{dong_ngoac} Nhập Tên File Lưu Thông Tin: ")
    if file_name.strip():
        if not file_name.endswith(".txt"):
            file_name += ".txt"
        break
    else:
        print(f"{mo_ngoac_do}!{dong_ngoac} Tên File Không Được Để Trống. Vui Lòng Nhập Lại!")

while True:
    try:
        delay = int(input(f"{mo_ngoac}*{dong_ngoac} Nhập Thời Gian Delay (Trên 180 Giây): "))
        if delay > 10:
            break
        else:
            print(f"{mo_ngoac_do}!{dong_ngoac} Delay Phải Lớn Hơn 179 Giây. Vui Lòng Nhập Lại!")
    except ValueError:
        print(f"{mo_ngoac_do}!{dong_ngoac} Nội Dung Nhập Không Hợp Lệ!")

print(thanh)

for _ in range(account_count):
    create_account()
    
    print(f"Chờ {delay} Giây...", end='')
    for remaining in range(delay, 0, -1):
        print(f"\r{mo_ngoac}*{dong_ngoac} Vui Lòng Đợi: {remaining} Giây", end='', flush=True)
        time.sleep(1)
    print()
    print(thanh)

print(f"{mo_ngoac}✓{dong_ngoac} Tất Cả Thông Tin Đã Được Lưu Vào File: {xanhchuoi}{file_name}{resetmau}")
sys.exit()
