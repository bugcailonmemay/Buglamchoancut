import time
from time import strftime
import os
import sys
import requests
import json
from time import sleep
from datetime import datetime, timedelta
import base64
import subprocess
from pystyle import Colors, Colorate

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
print ("╔═════════════════════╗")
print ("║  Tool Trao Đổi Sub  ║")
print ("╚═════════════════════╝")

print("[</>] Nhập Số [1.1] TDS TIKTOK >>CLICK<< ")
print("[</>] Nhập Số [1.2] TDS TIKTOK & TIKTOK NOW >>CLICK<<")
print("[</>] Nhập Số [1.3] TDS Facebook V1 >>VIP<< ")
print("[</>] Nhập Số [1.4] TDS Facebook V2 >>update<<")
print("[</>] Nhập Số [1.5] TOOL ĐỔI MK TĐS >>ON<<")

print("════════════════════════════════════════════════  ")
print ("╔════════════════════════╗")
print ("║Tool Tiện Ích Facebook  ║")
print ("╚════════════════════════╝")
print("[</>] Nhập Số [2.1] Tool Reg Page >>ON<<")
print("[</>] Nhập Số [2.2] Tool Reg Nick Facebook NVR >>ON<<")
print("[</>] Nhập Số [2.3] Tool Tạo Mail 10P >>ON<<")
print("[</>] Nhập Số [2.4] Tool Share Ảo Cookie >>ON<<")
print("[</>] Nhập Số [2.5] Tool Share Ảo Pro5 >>ON<<")
print("[</>] Nhập Số [2.6] Tool Get ID >>ON<<")

print("════════════════════════════════════════════════  ")
print ("╔═══════════════════╗")
print ("║    TOOL ENCODE    ║")
print ("╚═══════════════════╝")
print("[</>] Nhập Số [3.1] Tool Encode V1 >>VIP<<")
print("[</>] Nhập Số [3.2] Tool Encode V2 >>ON<<")
print("════════════════════════════════════════════════  ")
print ("╔═══════════════════╗")
print ("║    TOOL NGHỊCH    ║")
print ("╚═══════════════════╝")
print("[</>] Nhập Số [4.1] Tool Tài Xỉu >>ON<<")
print("[</>] Nhập Số [4.2] Tool Fake CCCD >>VIP<<")
print("[</>] Nhập Số [4.3] Tool Spam SMS >>ON<<")

print("════════════════════════════════════════════════  ")
print ("╔═══════════════════╗")
print ("║    TOOL BUFF      ║")
print ("╚═══════════════════╝")
print("[</>] Nhập Số [5.1] Tool Buff TikTok >>VIP<<")

print ("╔═════════════════════╗")
print ("║ Tool Tương Tác Chéo ║")
print ("╚═════════════════════╝")
print("[</>] Nhập Số [6.1] TTC FACEBOOK >>VIP<<")
print("[</>] Nhập Số [00] THOÁT TOOL")

print("════════════════════════════════════════════════  ")
chon = str(input('[</>] Nhập Số \033[1;37m: '))


if chon == '00' :
    exec(requests.get('https://raw.githubusercontent.com/bugcailonmemay/Buglamchoancut/refs/heads/main/out.py').text)
    #tool tđs
if chon == '1.1':    
    exec(requests.get('https://raw.githubusercontent.com/bugcailonmemay/Buglamchoancut/refs/heads/main/tdsv1.py').text)    
if chon == '1.2':
    exec(requests.get('https://raw.githubusercontent.com/bugcailonmemay/Buglamchoancut/refs/heads/main/tdstik.py').text)
if chon == '1.3' :
    exec(requests.get('https://raw.githubusercontent.com/bugcailonmemay/Buglamchoancut/refs/heads/main/Tds.py').text) 
if chon == '1.4' :
    exec(requests.get('https://raw.githubusercontent.com/bugcailonmemay/Buglamchoancut/refs/heads/main/Tdsv1.py').text) 
elif chon == '1.5' : 
 exec(requests.get('https://raw.githubusercontent.com/bugcailonmemay/Buglamchoancut/refs/heads/main/mktds.py').text) 
#tool Facebook
elif chon == '2.1' :
 exec(requests.get('https://raw.githubusercontent.com/bugcailonmemay/Buglamchoancut/refs/heads/main/regpage.py').text)
elif chon == '2.2' :
 exec(requests.get('https://raw.githubusercontent.com/bugcailonmemay/Buglamchoancut/refs/heads/main/fbnvr.py').text)
if chon == '2.3' :
    exec(requests.get('https://raw.githubusercontent.com/bugcailonmemay/Buglamchoancut/refs/heads/main/mail10p.py').text)
if chon == '2.4' :
    exec(requests.get('https://raw.githubusercontent.com/bugcailonmemay/Buglamchoancut/refs/heads/main/aocoki.py').text)
if chon == '2.5' :
    exec(requests.get('http://tienich.x10.bz/sharepro5.py').text)    
if chon == '2.6' :
    exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/refs/heads/main/id.py').text)
#tool encode vip
if chon == '3.1' :
    exec(requests.get('https://raw.githubusercontent.com/bugcailonmemay/Buglamchoancut/refs/heads/main/enc.py').text)
if chon == '3.2' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/Encode-ejuly-DUYKHANH/main/encode.py').text)    
# nghịch tool    
if chon == '4.1' :
    exec(requests.get('https://raw.githubusercontent.com/bugcailonmemay/Buglamchoancut/refs/heads/main/tx.py').text)
if chon == '4.2' :
    exec(requests.get('https://raw.githubusercontent.com/bugcailonmemay/Buglamchoancut/refs/heads/main/cccd.py').text)    
if chon == '4.3' :
    exec(requests.get('https://raw.githubusercontent.com/bugcailonmemay/Buglamchoancut/refs/heads/main/text.py').text)        
#buff tiktok
if chon == '5.1' :
    exec(requests.get('https://raw.githubusercontent.com/bugcailonmemay/Buglamchoancut/refs/heads/main/tik.py').text)    
#ttc
elif chon == '6.1' :
    exec(requests.get('https://raw.githubusercontent.com/bugcailonmemay/Buglamchoancut/refs/heads/main/Ttc.py').text)        
else :
     exit()
