# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:23:40 2020

@author: andri
"""

### The first task was as follows:
#For example, suppose you have the following list:

#1-3 a: abcde
#1-3 b: cdefg
#2-9 c: ccccccccc

#Each line gives the password policy and then the password. 
#The password policy indicates the lowest and highest number of times a given letter 
#must appear for the password to be valid. 
#For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.



file = open("2Dec.txt","r")
liste = []

valid_pwd = 0

for line in file:
    line = line.replace("\n","")
    line = line.split(" ")
    liste.append(line)

for i in range(len(liste)):
    liste_range = []
    count = 0
    zahlen = liste[i][0].split("-")
    
    for numbers in zahlen:
        numbers = int(numbers)
        liste_range.append(numbers)
        
    for pwd in liste[i][2]:
        for char in pwd:
            if char == liste[i][1][:-1]:
                count += 1
    if count in range(liste_range[0],liste_range[1]+1):
        valid_pwd += 1
        
print(valid_pwd)


### The second task needed just a little ajustments:
#Each policy actually describes two positions in the password, 
#where 1 means the first character, 2 means the second character, and so on. 
#(Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
#Exactly one of these positions must contain the given letter. 
#Other occurrences of the letter are irrelevant for the purposes of policy enforcement.


file = open("2Dec.txt","r")
liste = []

valid_pwd = 0


for line in file:
    line = line.replace("\n","")
    line = line.split(" ")
    liste.append(line)

for i in range(len(liste)):
    liste_range = []
    count = 0
    zahlen = liste[i][0].split("-")
    
    for numbers in zahlen:
        numbers = int(numbers)
        liste_range.append(numbers)
    
    index_one = liste_range[0]-1
    index_two = liste_range[1]-1
    pwd = liste[i][2]

    if pwd[index_one] == liste[i][1][:-1] and pwd[index_two] != liste[i][1][:-1]:
        valid_pwd += 1
        
    elif pwd[index_two] == liste[i][1][:-1] and pwd[index_one] != liste[i][1][:-1]:
        valid_pwd += 1
           

print(valid_pwd)