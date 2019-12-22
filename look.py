from colorama import *
from os import *
script='''
 m       mmmm   mmmm   mmmmm m   m
 #      m"  "m m"  "m m"   " #  m"
 #      #    # #    # #      #m#
 #      #    # #    # #      #  #m
 #mmmmm  #mm#   #mm#   "mmm" #   "m
'''
menu='''
01:dos
02:exploits
'''
ddos='''
01:xerxes
02:xshell
03:goldeneye
'''
exploite='''
01:websploit
02:metasploit
03:routersploit
def dos():
    print(Fore.BLUE + ddos)
    dddos=input(look)
    if dddos == '01' or ddos == '1':
        system('pkg install clang')
        system('git clone https://github.com/XCHADXFAQ77X/XERXES')
    elif dddos == '02' or ddos == '2':
        system('pkg install perl')
        system('git clone https://github.com/Manisso/Xshell')
    elif dddos == '03' or ddos == '3':
        system('git clone https://github.com/jseidl/GoldenEye')
    else:
        print(Fore.YELLOW + 'command not found')
def exploit():
    print (Fore.BLUE + exploite)
    exp=input(look)
    if exp == '01' or exp == '1':
        system('git clone https://github.com/websploit/websploit')
    elif exp == '02' or exp == '2':
        system('pkg install metasploit')
    elif exp == '03' or exp == '3':
        system('git clone https://github.com/threat9/routersploit')
    else:
        print(Fore.RED + 'command not found')
look='root@look|> '
def bunner():
    global menu,script,ddos,exploite
    print(Fore.RED + script)
    print(Fore.BLUE + menu)
    vibor=input(look)
    if vibor == '01' or vibor == '1':
        dos()
    elif vibor == '02' or vibor == '2':
        exploit()
    else:
        print(Fore.RED + 'command not found')
bunner()
        
