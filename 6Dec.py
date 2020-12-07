# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 12:33:52 2020

@author: andri
"""


with open("6Dec.txt") as file:
    group = file.read().split("\n\n")
 
clean = []
summe = 0 
summe2 = 0   
    
for g in group:
    clean.append(g.split("\n"))
    
for group in clean:
    questions = []
    questions2 = []
    for p in range(len(group)):
        for char in group[p]:
            if char not in questions:
                questions.append(char)
                
    for q in questions:
        check = True
        for p in group:
            if q not in p:
                check = False
        if check == False:
            summe2 += 1
            
    summe += len(questions)

        
print(summe)
print(summe-summe2)
