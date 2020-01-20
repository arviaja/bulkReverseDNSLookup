#!/usr/bin/env python

"""revdnslookup.py: Reads an input file of IPv4 Addresses and returns a reverse DNS Lookup"""

__author__      = "Sebastian Varga"
__license__     = "GPL"

import socket

with open('iplist.txt') as f:
    for ip in f:
        try:
            resolvedIP = socket.gethostbyaddr(ip)
            print(ip)
        except:
            print("can't find reverse entry for IP "+ip, end='')
