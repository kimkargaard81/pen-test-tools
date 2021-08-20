#!/bin/python3

import socket #Used socket to connect one node to another in this script

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF-INET = IPv4, socket.SOCK_STREAM = Port
s.connect((HOST,PORT))
