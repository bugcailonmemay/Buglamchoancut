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
    

from urllib import response
import string
import random
import requests
import time
import os
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
import socket
import psutil
import signal
from pystyle import *       
from packaging import version
import time 
import os, sys
from pystyle import Write,Colors
import subprocess
from argparse import ArgumentParser
from colorama import Fore
from colorama import Style
from pystyle import Write,Colors
import subprocess

def get_ip():
    try:
        ip = socket.gethostbyname(requests.get("http://kiemtraip.com/raw.php").text.strip())
    except requests.exceptions.ConnectionError:
        print(f"{chars} \033[1;36;40m Lỗi Mạng !!!\033[1;37;40m")
        sys.exit()
    if ip in ['0.0.0.0']:
        print(f"{chars} \033[1;36;40mBật Mạng Lên Em Iu \033[1;31;40m<3\033[1;37;40m")
        sys.exit()
    return ip

ip = get_ip()    
times = str(time.strftime("%H:%M:%S"))    
ngay = str(time.strftime("%d"))
thang = str(time.strftime("%m"))
nam = str(time.strftime("%Y"))
os.system("cls" if os.name == "nt" else "clear")
def banner():
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
[</>] GIỚI HẠN THIẾT BỊ : 1 🚦
[</>] NGƯỜI MUA : USER.....
[</>] KEY : NDK*********
[</>] Date Time ( {times} - {ngay}/{thang}/{nam} )
[</>] Ip ( {ip} )
════════════════════════════════════════════════  
                  [THÔNG BÁO]
>>>>TOOL ĐANG TRONG QUÁ TRÌNH PHÁT TRIỂN THÊM<<<<     
════════════════════════════════════════════════                                
"""

    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)
os.system("cls" if os.name == "nt" else "clear")
banner()
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
endpoint = 'https://dropmail.me/api/graphql/'
token = ''

def start(interval):
    request = queried_request(session_query())
    if not request.ok:
        raise Exception('Không thể hoàn thành yêu cầu: #' + str(request.status_code))
    response = request.json()
    session = response['data']['introduceSession']
    session_id = session['id']
    email = session['addresses'][0]['address']
    success('Địa chỉ email của bạn: ' + email)
    success('Đang làm mới hộp thư...')
    while True:
        mailbox = queried_request(mailbox_query(session_id)).json()
        mails = mailbox['data']['session']['mails']
        if mails:
            success('Đã nhận mail:')
            print('-----------------------\n')
            print(mails[0]['text'])
            return
        else:
            time.sleep(interval)

def session_query():
    return 'mutation {introduceSession {id, addresses{address}}}'

def mailbox_query(id):
    return 'query ($id: ID!){session(id:$id) {mails{downloadUrl, text}}}&variables={"id":"' + id + '"}'

def get_token(chars):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=chars))

def queried_request(body):
    query = '?query=' + body
    return requests.get(endpoint + token + query)

def success(str, as_input=False):
    output = f'[</>] {str}'
    if as_input:
        input(output)
    else:
        print(output)

def error(str, e='', as_input=False):
    output = f'[ERROR] {str}: {e}'
    if as_input:
        input(output)
    else:
        print(output)

parser = ArgumentParser()
parser.add_argument('-i', '--interval', metavar='interval', type=int, nargs=1, help='Khoảng thời gian làm mới (s)')
args = parser.parse_args()

if __name__ == '__main__':
    print(token)
    try:
        token = get_token(8)
        interval = 3
        if args.interval:
            interval = args.interval[0]
        start(interval)
    except Exception as e:
        error('LỖI TÙM LUM', e, True)