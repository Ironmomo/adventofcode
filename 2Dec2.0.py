# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:26:20 2020

@author: andri
"""

import re

file = open("2Dec.txt","r")

lines = file.readlines()

pattern = "([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)"
valid_pwd = 0
valid_pwd2 = 0

for i in lines:
    line = re.search(pattern, i)
    min_amount = int(line.group(1))
    max_amount = int(line.group(2))
    char = line.group(3)
    password = line.group(4)
    count = password.count(char)
    if count >= min_amount and count <= max_amount:
        valid_pwd += 1
        
    #Part Two
        
    if password[min_amount-1] == char and password[max_amount-1] != char:
        valid_pwd2 += 1
        
    elif password[max_amount-1] == char and password[min_amount-1] != char:
        valid_pwd2 += 1
        
        
print(valid_pwd)
print(valid_pwd2)