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
    

import sqlite3
import random
import socket
import datetime
import time
import os
import requests 
import sys 
from time import sleep
from colorama import init, Fore, Style

# Khởi tạo colorama để hỗ trợ màu sắc trên Windows
init(autoreset=True)

# Kết nối database
conn = sqlite3.connect("taixiu.db")
cursor = conn.cursor()

# Tạo bảng lưu thông tin người chơi
cursor.execute('''
    CREATE TABLE IF NOT EXISTS players (
        ip TEXT PRIMARY KEY,
        name TEXT,
        money INTEGER
    )
''')
conn.commit()

# Lấy địa chỉ IP
def get_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "Unknown"

def check_connection():
    try:
        response = requests.get("https://www.google.com.vn", timeout=3)        
    except (requests.exceptions.ReadTimeout, requests.ConnectionError):
        print("Vui lòng kiểm tra kết nối mạng !!!")
        sys.exit()
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"Lỗi: {str(e)}")
check_connection()   

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

# Hiển thị thông tin người chơi
def show_info(name, money, ip):
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    print("╔" + "═" * 40 + "╗")
    print(f"║ 👤 Người Chơi: {name:<25}║")
    print(f"║ 💰 Tiền Hiện Có: {money:,} VND  ║")
    print(f"║ 📅 Ngày: {today:<25}║")
    print(f"║ 🌐 IP: {ip:<25}║")
    print("╚" + "═" * 40 + "╝" + Style.RESET_ALL)

# Kiểm tra và cho vay tiền
def check_and_loan(name, money, ip):
    if money <= 0:
        while True:
            show_info(name, money, ip)  # Hiển thị thông tin trước khi hỏi vay
            try:
                loan = input("\n💰 Vay Của Nhà Cái: (Nhập số tiền từ 1k đến 500k): ").replace("k", "000")
                loan = int(loan)
                
                if 1_000 <= loan <= 500_000:
                    money += loan
                    print(f"💵 Người chơi {name} đã vay nhà cái {loan:,} VND!!")
                    cursor.execute("UPDATE players SET money=? WHERE ip=?", (money, ip))
                    conn.commit()
                    break
                else:
                    print("❌ Chỉ có thể vay từ 1,000 đến 500,000 VND! Vui lòng nhập lại.")
            except ValueError:
                print("❌ Vui lòng nhập số tiền hợp lệ!")

    return money

# Chơi tài xỉu
def play_game(name, money, ip):
    while True:
        show_info(name, money, ip)
        bet = input("🎲 Nhập số tiền cược (hoặc 'exit' để thoát): ").lower()
        if bet == "exit":
            print("Thoát game...")
            break

        # Xử lý nhập tiền
        try:
            bet = int(bet.replace("k", "000"))  # Đổi 1k -> 1000
            if bet > money or bet <= 0:
                print("❌ Số tiền không hợp lệ! Vui lòng nhập lại.")
                continue
        except ValueError:
            print("❌ Vui lòng nhập số hợp lệ!")
            continue

        # Chọn tài/xỉu
        choice = input("🎲 Xin mời bạn chọn (Tài/Xỉu): ").strip().lower()
        if choice not in ["tài", "xỉu", "tai", "xiu"]:
            print("❌ Lựa chọn không hợp lệ!")
            continue

        # Chuẩn hóa kết quả thành "Tài" hoặc "Xỉu"
        choice = "Tài" if choice in ["tài", "tai"] else "Xỉu"

        # Hiệu ứng gieo xúc xắc
        print("\n⏳ Nhà cái sẽ lắc xúc xắc sau 3 giây...")
        for i in range(3, 0, -1):
            print(f"🎲 Xúc xắc đang gieo... {i}s")
            time.sleep(1)

        # Quay xúc xắc
        dice = [random.randint(1, 6) for _ in range(3)]
        total = sum(dice)
        result = "Tài" if total >= 11 else "Xỉu"

        print(f"\n🎲 Xúc xắc: {dice} => Tổng: {total} => {Fore.GREEN if result == 'Tài' else Fore.RED}{result}")

        # Kiểm tra kết quả
        if choice == result:  
            money += bet * 2  # ✅ Nhân đôi tiền cược khi thắng
            print(f"🎉 Bạn thắng! Nhận {bet * 2:,} VND. Tiền hiện có: {money:,} VND")
        else:
            money -= bet  # ❌ Mất đúng số tiền đã đặt cược
            print(f"💸 Thua rồi :((( Tiền còn lại: {money:,} VND")

        # Kiểm tra nếu tiền về 0 => Hiển thị tùy chọn vay tiền
        money = check_and_loan(name, money, ip)

        # Cập nhật tiền trong database
        cursor.execute("UPDATE players SET money=? WHERE ip=?", (money, ip))
        conn.commit()

# Lấy thông tin người chơi hoặc tạo mới
def get_or_create_player():
    ip = get_ip()
    cursor.execute("SELECT name, money FROM players WHERE ip=?", (ip,))
    player = cursor.fetchone()

    if player:
        name, money = player
        print(f"🎉 Chào mừng trở lại, {name}!")
    else:
        name = input("👤 Nhập tên người chơi: ")
        money = 100000  # 100k khi tạo mới
        cursor.execute("INSERT INTO players (ip, name, money) VALUES (?, ?, ?)", (ip, name, money))
        conn.commit()
        print(f"✅ Tạo tài khoản mới cho {name} với 100k!")

    # Kiểm tra và xử lý vay tiền nếu cần
    money = check_and_loan(name, money, ip)

    return name, money, ip

# Chạy game
os.system("cls" if os.name == "nt" else "clear")
banner()
name, money, ip = get_or_create_player()
play_game(name, money, ip)

# Đóng kết nối
conn.close()
