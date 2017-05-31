#!/usr/bin/python
import httplib
import socket
import os

def domain():
    domainnames = ['iuqerfsodp9ifjaposdfjhgosurijfaewrwergwea.com','Rphjmrpwmfv6v2e.onion','Gx7ekbenv2riucmf.onion','57g7spgrzlojinas.onion','xxlvbrloxvriy2c5.onion','76jdd2ir2embyv47.onion','cwwnhwhlz52maqm7.onion']
    for domainname in domainnames:
	try:
            conn = httplib.HTTPConnection(domainname)
            conn.request("GET", "/index.html")
            conn.close
	except:
	    continue
    print 'Domainname connected'

def c2():
    address = ('2.3.69.209', 9001)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
    	s.connect(address)
     	s.close()
    except:
     	print 'C2 connected'


def scan():
    os.system('nmap -iR 1000 -P0 -n -p 445')    
def main():
    domain()
    c2()
    scan()

if __name__ == '__main__':
    main()
