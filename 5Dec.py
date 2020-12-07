# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 21:43:45 2020

@author: andri
"""

file = open("5Dec.txt","r")
boardingpass = []
blocked_seat = []
seat_id = []

for i in file:
    boardingpass.append(i.strip())
    
for i in boardingpass:
    seat_row = [0,127]
    seat_col = [0,7]
    row = 0
    col = 0
    for j in range(len(i)):
        char = i[j]
        difc = round((seat_col[1] - seat_col[0])/2)  
        dif = round((seat_row[1] - seat_row[0])/2)
        
        if j == 6:
            if char == "B":
                seat_row[0] += dif
                row = seat_row[1]
            elif char == "F":
                seat_row[1] -= dif
                row = seat_row[0]
        elif j == 9:
            if char == "R":
                seat_col[0] += difc
                col = seat_col[1]
            elif char == "L":
                seat_col[1] -= difc
                col = seat_col[0]
                
        else:        

            if char == "B":
                seat_row[0] += dif
            
            elif char == "F":
                seat_row[1] -= dif
                
            elif char == "R":
                seat_col[0] += difc
            
            elif char == "L":
                seat_col[1] -= difc
          
    blocked_seat.append((row,col))

max_ID = 0

for i in blocked_seat:
    ID = i[0]*8+i[1]
    seat_id.append(ID)
    if ID >= max_ID:
        max_ID = ID
        
print(max_ID)
        
seat_id = sorted(seat_id)

for i in range(seat_id[0],seat_id[-1]+1):
    if i not in seat_id:
        print(i)



