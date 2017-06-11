#!/usr/bin/python
#! -*- coding: utf-8 -*-
import os
import sys

def main():
    os.system('tcpreplay --topspeed -i eth0 ./pcap/*.pcap')
    sys.exit(0)

if __name__ == '__main__':
    main()
