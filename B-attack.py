



import os, sys, subprocess,time
import os, sys, json, urllib, re
from time import sleep
os.system("clear")
reload(sys)
sys.setdefaultencoding("utf-8")

# Console colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[1m'  # bold
RR = '\033[3m'  # greencolor

def logo():
 print("""\033[1m
 \033[33m______       _ _    ___  _   _             _    
 \033[33m| ___ \     | | |  / _ \\| | | |           | |   
 | |_/ /_   _| | | / /_\ \ |_| |_ __ _  ___| | __
 | ___ \ | | | | | |  _  | __| __/ _` |/ __| |/ /
\033[32m | |_/ / |_| | | | | | | | |_| || (_| | (__|   <
 \____/ \__,_|_|_| \_| |_/\__|\__\__,_|\___|_|\_\\

\n\t     \033[31m[_Location Catcher_]
 \n\033[0m\033[1m
\t \033[33m[-] \033[0mPlatform : \033[33mAndroid Termux
\t \033[1m\033[33m[-] \033[0mName     : \033[33mBull Attack
\t \033[1m\033[33m[-] \033[0mSite     : \033[33mwww.bhai4you.net
\t \033[1m\033[33m[-] \033[0mCoded by :\033[1m \033[33m[  \033[32mParixit \033[33m ]
\t \033[1m\033[33m[-] \033[0mSec.Code : \033[33m8h4i\033[0m
  """)


logo()
  

print("""\n\n\n\t\033[33m\033[1m   <===[\033[32m:.Commands.:\033[33m]===>\033[0m
       \n\n1. B-Attack    : Website or IP Location Hacker
       \n2. exit        : Exit Bull Attack...
\n\n\033[1m\033[32mtype : 1 or 2
       \033[0m""")
def help():
	print("""\n\n
  Commands :
       \n\n1. web     : Website Location Hacker
       \n2. exit        : Exit Bull Attack

\n\n\n type : 1 or 2
       """)





	

bull = raw_input("\n\n[*] Bull Attack \033[1m\033[33m===>\033[0m ")
if bull == "help":
            help()

elif bull == '1':
	print "\n\n\t\033[33m\033[1m <===[\033[32m:.Website or IP Hacker.:\033[33m]===>\033[0m\n\n\neg. Target\n\n\033[1m\033[33mWebsite\033[0m : www.bhai4you.net\n\n\033[1m\033[33mIp\033[0m      : 74.125.130.121"
IP = raw_input("\n\n[*] Website or IP \033[1m\033[33m===>\033[0m")
print "\nHacking\033[1m\033[33m ===> %s" % (IP)
IP2 = IP.split(".")
if IP in ["self", "myself"]:
  urllib.urlretrieve("https://api.ipify.org?format=json", 'data.json')
  file = open('data.json')
  data = json.load(file)
  IP = data["ip"]
urllib.urlretrieve("http://ip-api.com/json/%s" %IP, 'data.json')
file = open('data.json')
data = json.load(file)
if data["status"] != "success": 
  	print "\nHey Bro Sorry!!!  -Please Enter Correct Details...\n\n\033[1m\033[33m     [*] I Am Proud To Be An \033[1m\033[31mIn\033[1m\033[0mdi\033[1m\033[32man\033[33m [*]\n\n\t Advice For \033[1m\033[31mIn\033[1m\033[0mdi\033[1m\033[32man\033[1m\033[33m People \n\n\n\033[1m\033[32m[\033[33m==>\033[32m Mere Bhai True Website or IP Enter Kar...!!!\033[33m <===\033[32m]\033[0m\n\n"
  	exit()


	
elif bull == '2' or bull == '02' or bull == 'exit':
	print "\033[1m\033[31m\n\t\t[!] Exit Bull Attack...     \n\n\t\033[1m\033[32m\033[0m"
	sys.exit()
	
else:
	print "\n\n\n\t[!] B-attack : \033[32mHacked!!!\033[0m\n\n"

for k in data:
    if data[k] == "": data[k] = "Unknown"
print "\n       *** .: %s :. ***\n\n\n" %data["query"]
print "\nONLINE                         \033[32m\033[1m%s\033[0m    " %data["status"]
print "\nISP                            \033[1m\033[32m%s\033[0m    "%data["isp"]
print "\nORG. NAME                      \033[32m\033[1m%s\033[0m" %data["org"]
print "\nCITY                           \033[32m\033[1m%s\033[0m    " %data["city"]
print "\nCITY TIMEZONE                  \033[32m\033[1m%s\033[0m    " %data["timezone"]
print "\nREGION NAME                    \033[32m\033[1m%s\033[0m" %data["regionName"]
print "\nREGION CODE                    \033[32m\033[1m%s,\033[0m" %data["region"]
print "\nCOUNTRY                        \033[32m\033[1m%s,\033[0m" %data["country"]
print "\nCOUNTRY CODE                   \033[32m\033[1m%s,\033[0m" %data["countryCode"]
print "\nZIP CODE                       \033[32m\033[1m%s\033[0m" %data["zip"]
print "\nLATITUDE                       \033[32m\033[1m%s\033[0m" %data["lat"]
print "\nLONGITUDE                      \033[32m\033[1m%s\033[0m" %data["lon"]
print "\nAS NUMBER/NAME                 \033[32m\033[1m%s\033[0m" %data["as"]
            

print "\n\n\n\n\033[1m\033[32m<=======[ \033[33m\033[1m\033[33m:.Author \033[1m\033[31m:\033[33m Sutariya Parixit.:\033[32m ]=======>\n\n\033[0m"
os.system('rm *.json')
	
sys.exit()
