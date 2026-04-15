import time
import sys
import os
from colorama import Fore, Style, init

# تهيئة الألوان
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_big_hak():
    hak_art = f"""
{Fore.LIGHTGREEN_EX}{Style.BRIGHT}
      ██╗  ██╗ █████╗ ██╗  ██╗
      ██║  ██║██╔══██╗██║ ██╔╝
      ███████║███████║█████╔╝ 
      ██╔══██║██╔══██║██╔═██╗ 
      ██║  ██║██║  ██║██║  ██╗
      ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
    {Fore.LIGHTBLACK_EX}--- ROOT ACCESS TERMINAL v9.4.1 ---
    """
    print(hak_art)

def long_initial_loading():
    """شريط تحميل طويل يظهر لمرة واحدة فقط في البداية"""
    bar_length = 50
    print(f"\n{Fore.WHITE}[SYSTEM] INITIALIZING GLOBAL EXPLOIT DATABASE...")
    for i in range(0, 101):
        filled = int(bar_length * i // 100)
        bar = "█" * filled + "░" * (bar_length - filled)
        sys.stdout.write(f'\r{Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}{bar}{Fore.LIGHTBLACK_EX}] {Fore.WHITE}{i}%')
        sys.stdout.flush()
        time.sleep(0.06)
    print(f"\n{Fore.LIGHTGREEN_EX}[+] CORE MODULES LOADED.\n")

def radio_scanner(label="SCANNING", duration=4):
    """مؤشر راديو صغير يتحرك ذهاباً وإياباً"""
    width = 20
    start = time.time()
    while (time.time() - start) < duration:
        for pos in range(width):
            slider = "─" * pos + "█" + "─" * (width - pos - 1)
            sys.stdout.write(f'\r{Fore.LIGHTBLACK_EX}    [{Fore.LIGHTGREEN_EX}{slider}{Fore.LIGHTBLACK_EX}] {Fore.WHITE}{label}...')
            sys.stdout.flush()
            time.sleep(0.04)
        for pos in range(width-1, -1, -1):
            slider = "─" * pos + "█" + "─" * (width - pos - 1)
            sys.stdout.write(f'\r{Fore.LIGHTBLACK_EX}    [{Fore.LIGHTGREEN_EX}{slider}{Fore.LIGHTBLACK_EX}] {Fore.WHITE}{label}...')
            sys.stdout.flush()
            time.sleep(0.04)
    sys.stdout.write('\r' + ' ' * 50 + '\r') # مسح سطر الراديو بعد الانتهاء

def run_simulator():
    groups = [
        ["http://89.1.82.42:80", "http://176.95.177.220:8086", "http://5.10.10.199:50000", "http://89.107.164.96:8000", "http://217.91.0.13:80", "http://185.146.206.159:80", "http://80.152.138.183:80", "http://130.180.21.202:8081", "http://80.147.147.157:50001", "http://80.153.205.89:81", "http://217.86.173.126:80", "http://87.128.61.124:8081", "http://87.128.61.124:8084", "http://87.128.61.124:8083", "http://5.100.32.48:8001", "http://191.101.165.194:8888", "http://87.140.50.57:82", "http://37.24.101.118:80", "http://87.128.105.199:88", "http://130.180.86.110:8082", "http://80.151.137.153:80", "http://80.152.149.140:50001", "http://80.88.23.120:8080", "http://80.88.23.120:80", "http://217.5.234.146:80", "http://93.241.243.144:50001"], 
        ["http://81.247.199.120:8060", "http://81.82.251.41:8082", "http://94.110.74.26:80", "http://81.83.82.38:8080", "http://87.66.9.180:3000", "http://84.196.142.208:8080", "http://84.195.88.137:8080", "http://81.82.193.69:10001", "http://193.190.230.96:80"],
        ["http://168.0.126.43:8001", "http://177.36.59.165:80", "http://143.106.161.110:80"],
        ["http://179.62.210.138:8088", "http://190.210.250.149:91", "http://190.15.193.92:8083", "http://181.171.25.136:80"],
        ["http://45.80.27.109:80", "http://109.166.169.204:9000", "http://92.85.14.184:83", "http://86.123.146.149:81", "http://86.123.146.147:81", "http://185.132.173.115:81", "http://185.132.173.115:83", "http://86.122.62.167:81", "http://86.121.159.16:80", "http://188.27.232.88:8080", "http://109.99.208.157:8080", "http://82.77.203.219:8080", "http://109.102.24.214:8080", "http://82.76.133.139:80", "http://92.85.54.73:80", "http://5.2.205.219:8083", "http://81.180.37.123:80", "http://86.35.219.6:2000", "http://109.103.248.185:82", "http://82.78.229.98:3000", "http://92.87.123.82:83", "http://86.35.219.6:2002", "http://92.81.22.22:2000", "http://188.173.25.246:88", "http://82.76.145.217:80", "http://82.78.92.4:80", "http://86.127.212.219:80", "http://86.127.212.113:80", "http://86.127.101.19:80", "http://89.121.196.99:82", "http://82.79.74.61:8080", "http://109.166.208.204:80", "http://89.39.108.179:8080"]
    ]

    clear_screen()
    print_big_hak()
    
    # واجهة الدخول
    print(f"{Fore.LIGHTBLACK_EX}[" + f"{Fore.WHITE} AUTHENTICATION REQUIRED " + f"{Fore.LIGHTBLACK_EX}]")
    user = input(f"{Fore.WHITE}root@hak-system:~# login: {Fore.LIGHTGREEN_EX}")
    pw = input(f"{Fore.WHITE}root@hak-system:~# password: {Fore.LIGHTBLACK_EX}")
    
    # ظهور شريط التحميل الطويل لمرة واحدة فقط هنا
    long_initial_loading()

    for cycle in range(1, 3):
        if cycle == 2:
            print(f"\n{Fore.YELLOW}[!] STARTING SECOND PASS - RE-SCANNING ALL NODES...")
            time.sleep(1)

        for idx, group in enumerate(groups, 1):
            print(f"\n{Fore.RED}[!] ACCESSING NODE_{idx} (SWEEP {cycle}/2)")
            # استخدام الراديو الصغير هنا لبقية الوقت
            radio_scanner("SEARCHING", duration=3)
            
            for url in group:
                print(f"{Fore.LIGHTGREEN_EX}[DUMP] >> {url}")
                time.sleep(0.03)
            
            if idx < len(groups):
                time.sleep(0.5)

    print(f"\n{Fore.WHITE}{Style.BRIGHT}>>> ALL CYCLES COMPLETED. LOGS SAVED.")
    print(f"{Fore.LIGHTBLACK_EX}>>> CONNECTION TERMINATED.")

if __name__ == "__main__":
    try:
        run_simulator()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] TERMINATED.")
