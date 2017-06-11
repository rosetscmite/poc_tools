#!/usr/bin/python

import os
import sys

def main():
	os.system('apt-get install figlet -y')
	os.system('chmod o+x auto_attack.py')
	os.system('chmod o+x pcap_review.py')
	os.system('chmod -R o+x hotcase')

if __name__ == '__main__':
	main()
