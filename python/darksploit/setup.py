import os
import time, sys, random
os.system("apt install python -y && pip install colorama")
from colorama import Fore

os.system("clear")
print('\n\n\n\n\n')

def babi(am):
  for e in am:
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.100)

babi(Fore.RED + '...AEVSPLOİT KURULUYOR...')
time.sleep(1)
os.system("cd ~ && rm -rf .bash_history .cache && clear")

print(Fore.BLUE + '''
----------------------------------
''' + Fore.RED + '''Güncelleme Paketleri Yükleniyor...''' + Fore.BLUE + '''
----------------------------------''')
print()
print(Fore.WHITE + "apt purge game-repo")
print(Fore.RED)

os.system("apt purge game-repo -y")

###

print()
print(Fore.WHITE + "apt update")
print(Fore.RED)

os.system("apt update -y")

###

print()
print(Fore.WHITE + "apt upgrade")
print(Fore.RED)

os.system("apt upgrade -y")

###

print()
print(Fore.WHITE + "apt-get upgrade && apt-get update")
print(Fore.RED)

os.system("apt-get upgrade && apt-get update -y")

###

print()
print(Fore.WHITE + "pkg update & pkg up & pkg upgrade")
print(Fore.RED)

os.system("pkg update -y && pkg up -y && pkg upgrade -y")

###

print(Fore.BLUE + '''
----------------------------------
''' + Fore.RED + '''Gerekli Paketler Yükleniyor...''' + Fore.BLUE + '''
----------------------------------''')

###

print()
print(Fore.WHITE + "git paketi yükleniyor...")
print(Fore.RED)

os.system("apt install git -y")

###

print()
print(Fore.WHITE + "python paketi yükleniyor...")
print(Fore.RED)

os.system("apt install python -y")

###

os.system("apt install termux-api -y")
os.system("apt install figlet -y")

os.system("apt install figlet -y")
os.system("mkdir ~/.termux/")
os.system("rm -rf $PREFIX/etc/motd")
os.system("rm -rf $PREFIX/etc/motd-playstore")
z = "/data/data/com.termux/files/usr/share/"
os.system("cd %s && rm -rf %sfiglet-fonts && rm -rf %sfiglet && mkdir %sfiglet && git clone https://github.com/xero/figlet-fonts && mv %sfiglet-fonts/* %sfiglet && rm -rf %sfiglet-fonts/"%(z,z,z,z,z,z,z))

print(Fore.BLUE + '''
----------------------------------
''' + Fore.RED + '''Gerekli Modüller Yükleniyor...''' + Fore.BLUE + '''
----------------------------------''')
print()
print(Fore.GREEN + "!!! Lütfen Durdurmayınız Aksi Taktirde Tool Çalışmaz Bu Yüklenenler Tool İçin Önemli. !!!")
time.sleep(3)
print()

###

os.system("pip install colorama")
os.system("pip install random")
os.system("pip install pyfiglet")
os.system("pip install bs4 && pip install beautifulsoup4")
os.system("pip install requests")
os.system("pip install user_agent")
os.system("pip install telebot")
os.system("pip install tqdm")
os.system("pip install qrcode")
os.system("pip install certifi==2020.6.20")
os.system("pip install chardet")
os.system("pip install idna")
os.system("pip install requests")
os.system("pip install urllib3")
os.system("pip install pyqrcode")
os.system("pip install pypng")
os.system("pip install wordlist")
os.system("pip install readchar")
os.system("pip install pytube")


print()
print(Fore.GREEN + "Lütfen Bu Uygulamayı Yükleyiniz...")
time.sleep(1.5)
os.system("xdg-open https://play.google.com/store/apps/details?id=com.termux.api")
print()
time.sleep(0.1)
print()
time.sleep(0.1)
print()
time.sleep(0.1)
print()
time.sleep(0.1)
print()
print(Fore.RED + "Tool Kullanıma Hazır.")
print()
time.sleep(0.1)
print()
time.sleep(0.1)
print()
time.sleep(0.1)
print()
time.sleep(0.1)

with open("/data/data/com.termux/files/usr/etc/bash.bashrc","a+") as dosya:
 dosya.write('\n\nalias aev="cd && cd Aevsploit-Assistant && python aevsploit.py"\n')
 dosya.write('alias Aev="cd && cd Aevsploit-Assistant && python aevsploit.py"\n')
 dosya.write('alias AEV="cd && cd Aevsploit-Assistant && python aevsploit.py"\n')
dosya.close()

os.system("source data/data/com.termux/files/usr/etc/bash.bashrc")

try:
 a = input("Devam Etmek İçin Entere Basınız")

 if a == True:
  os.system("xdg-open https://t.me/termux_egitim/86")
 else:
  os.system("xdg-open https://t.me/termux_egitim/86")
  
 print()
 print(Fore.WHITE + "Toolu Başlatmak İçin" + Fore.RED + " aev " + Fore.WHITE + "Yazın")
 print()
 exit()
  
except KeyboardInterrupt:
 os.system("xdg-open https://t.me/termux_egitim/86")