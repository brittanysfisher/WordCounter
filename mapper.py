#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys 
import re
  
for line in sys.stdin: 
    line = line.strip() 
    words = re.findall(r"[a-zA-Z]+", sys.stdin.readline())
    for word in words:
        print('%s\t%s' % (word, 1))
