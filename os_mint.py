
#cd $HOME/selenium_course; python os_mint.py
# https://andreyex.ru/yazyk-programmirovaniya-python/vypolnenie-komand-obolochki-s-python/

import os
import time 


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")





myCmd = 'sudo ls -la' 
os.system (myCmd)

#myCmd = "ping -c 1 8.8.8.8 &> /dev/null && echo success || echo fail & sudo service network-manager restart"
myCmd = "ping -c 1 8.8.8.8 &> /dev/null && echo success || sudo service network-manager restart"
myCmd = "ping -c 1 8.8.8.8 > txt.txt"
#myCmd = "ping -c 1 8.8.8.8"
i = 0
errors = 0
while True:
    time.sleep(2)
    i += 1
    #print(i)
    print(f"{bcolors.WARNING}==={i}==={bcolors.ENDC}")
    os.system(myCmd)
    f = open("txt.txt")
    read = f.read()
    #print(f.read())
    f.close()
    if not "time=" in read:
        os.system("sudo service network-manager restart")
        print(f"{bcolors.FAIL}Try reload{bcolors.ENDC}")
        errors =+ 1
    else:
        print(f"{bcolors.OKGREEN}OK. Continue... {errors}{bcolors.ENDC}")
    

	#myCmd = os.popen(myCmd).read()
	#print(myCmd)

