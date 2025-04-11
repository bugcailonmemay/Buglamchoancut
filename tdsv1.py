# Coded by NGUYỄN DUY KHÁNH
# YTB: REVIEW TOOL 247
import os
from time import sleep
from datetime import datetime

os.environ['TZ'] = 'Asia/Ho_Chi_Minh'

try:
    import requests
except:
    os.system("pip3 install requests")
    import requests

headers = {
    'authority': 'traodoisub.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'user-agent': 'traodoisub tiktok tool',
}

def login_tds(token):
    try:
        r = requests.get(f'https://traodoisub.com/api/?fields=profile&access_token={token}', headers=headers, timeout=5).json()
        if 'success' in r:
            os.system('clear')
            print(f"Đăng nhập thành công!\nUser: {r['data']['user']} | Xu hiện tại: {r['data']['xu']}")
            return 'success'
        else:
            print("Token TDS không hợp lệ, hãy kiểm tra lại!\n")
            return 'error_token'
    except:
        return 'error'

def load_job(type_job, token):
    try:
        r = requests.get(f'https://traodoisub.com/api/?fields={type_job}&access_token={token}', headers=headers, timeout=5).json()
        if 'data' in r:
            return r
        elif "countdown" in r:
            sleep(round(r['countdown']))
            print(f"{r['error']}\n")
            return 'error_countdown'
        else:
            print(f"{r['error']}\n")
            return 'error_error'
    except:
        return 'error'

def duyet_job(type_job, token, uid):
    try:
        r = requests.get(f'https://traodoisub.com/api/coin/?type={type_job}&id={uid}&access_token={token}', headers=headers, timeout=5).json()
        if "cache" in r:
            return r['cache']
        elif "success" in r:
            print("------------------------------------------")
            print(f"Nhận thành công {r['data']['job_success']} nhiệm vụ | {r['data']['msg']} | {r['data']['xu']}")
            print("------------------------------------------")
            return 'error'
        else:
            print(r['error'])
            return 'error'
    except:
        return 'error'

def check_tiktok(id_tiktok, token):
    try:
        r = requests.get(f'https://traodoisub.com/api/?fields=tiktok_run&id={id_tiktok}&access_token={token}', headers=headers, timeout=5).json()
        if 'success' in r:
            os.system('clear')
            print(f"{r['data']['msg']}|ID: {r['data']['id']}")
            return 'success'
        else:
            print(f"{r['error']}\n")
            return 'error_token'
    except:
        return 'error'

os.system('clear')
banner = """
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
print(banner)

while True:
    try:
        with open('TDS.txt', 'r') as f:
            token_tds = f.read()
        cache = 'old'
    except FileNotFoundError:
        token_tds = input("Nhập token TDS: ")
        cache = 'new'

    for _ in range(3):
        check_log = login_tds(token_tds)
        if check_log == 'success' or check_log == 'error_token':
            break
        else:
            sleep(2)

    if check_log == 'success':
        if cache == 'new':
            with open('TDS.txt', 'w') as f:
                f.write(token_tds)
        break
    else:
        sleep(1)
        os.system('clear')

if check_log == 'success':
    while True:
        id_tiktok = input("Nhập ID tiktok: ")
        for _ in range(3):
            check_log = check_tiktok(id_tiktok, token_tds)
            if check_log == 'success' or check_log == 'error_token':
                break
            else:
                sleep(2)

        if check_log == 'success':
            break
        elif check_log == 'error_token':
            os.system('clear')
            print("ID tiktok chưa được thêm vào cấu hình, vào cấu hình rồi nhập lại!\n")
        else:
            os.system('clear')
            print("Lỗi server, vui lòng nhập lại!\n")

    while True:
        try:
            delay = int(input("Thời gian delay (giây): "))
            if delay > 1:
                break
            else:
                print("Delay tối thiểu là 3\n")
        except:
            print("Hãy nhập một số > 2\n")

    while True:
        try:
            max_job = int(input("Bao nhiêu nhiệm vụ dừng tool: "))
            if max_job > 9:
                break
            else:
                print("Tối thiểu là 10\n")
        except:
            print("Hãy nhập một số > 9\n")

    os.system('clear')

    type_load = 'tiktok_follow'
    type_duyet = 'TIKTOK_FOLLOW_CACHE'
    type_nhan = 'TIKTOK_FOLLOW'
    type_type = 'FOLLOW'

    dem_tong = 0

    while True:
        list_job = load_job(type_load, token_tds)
        sleep(2)
        if isinstance(list_job, dict):
            for job in list_job['data']:
                uid = job['id']
                link = job['link']
                os.system(f'termux-open-url {link}')
                check_duyet = duyet_job(type_duyet, token_tds, uid)

                if check_duyet != 'error':
                    dem_tong += 1
                    t_now = datetime.now().strftime("%H:%M:%S")
                    print(f'[{dem_tong}] | {t_now} | {type_type} | {uid}')

                if dem_tong == max_job:
                    break
                else:
                    for i in range(delay, -1, -1):
                        print(f'REVIEWTOOL247 : {i} giây', end='\r')
                        sleep(1)

        if dem_tong == max_job:
            print(f'Hoàn thành {max_job} nhiệm vụ!')
            break
