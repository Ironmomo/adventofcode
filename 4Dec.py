# -*- coding: utf-8 -*-

###Today we had to check passports for specific values and see if the input matches with the value
###The passport ends with an empty line after that a new passport comes. 
#First Part : A passport is valid if at least ecl pid byr iyr hcl eyr hgt is in the input. cid is optional
#Second Part : If the passport is valid like in the first part, the input had to match specific criteria.

import re
f = open("4Dec.txt","r")
p_u = f.read().split("\n\n")
pwd = []
count = 0
count2 = 0

def check_birth(s):
    try:
        s = int(s)
    except ValueError:
        return False
    else:
        if 1920 <= s <= 2002:
            return True

def check_issue(s):
    try:
        s = int(s)
    except ValueError:
        return False
    else:
        if 2010 <= s <= 2020:
            return True
        
def check_hcl(s):
    pattern = "#([a-z0-9]{6})"
    if re.search(pattern, s) and len(s) == 7:
        return True
    
def check_eyr(s):
    try:
        s = int(s)
    except ValueError:
        return False
    else:
        if 2020 <= s <= 2030:
            return True
        

def check_hgt(s):
    heigth = re.match(r"^(\d{1,})(cm|in)$",s)
    if heigth:
        if heigth[2] == "cm":
            if 150 <= int(heigth[1]) <= 193:
                return True
        if heigth[2] == "in":
            if 59 <= int(heigth[1]) <= 76:
                return True
            

value = {"ecl": lambda s: s in ["amb","blu","brn","gry","grn","hzl","oth"],
         "pid": lambda s: len(s) == 9 and s.isdigit(),
         "byr": check_birth,
         "iyr": check_issue,
         "hcl": check_hcl,
         "eyr": check_eyr,
         "hgt": check_hgt
         }



for i in p_u:
    pwd.append(i.replace("\n"," ").split(" "))
    
for p in pwd:
    d = dict(i.split(":") for i in p)
    check = True
    for v in value:
        if v not in d:
            check = False
    if check == True:
        count+=1
        check2 = True
        for v in value:
            valid = value[v]            
            if not valid(d[v]):
                check2 = False
        if check2:
            count2 += 1

print(count)
print(count2)




                
    