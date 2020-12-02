# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:34:15 2020

@author: andri
"""

###This is the first Task of adventofcode.com 2020
### First: Find two numbers out of a list of numbers which sum up to 2020 and multiplie them together 
###Second: Find three numbers out of a list of numbers which sum up to 2020 and multiplie them together

file = open("1Dec.txt","r")

liste = []
for i in file:
    liste.append(int(i))


def get_numbers(sum_up_to,list_of_num,operator):
    
    if operator == 1:
        if sum_up_to in list_of_num:
            return sum_up_to
        else:
            return 0


    for number in list_of_num:
        second_number = sum_up_to - number
        valid_num = get_numbers(second_number, list_of_num, operator-1)
        if valid_num > 0:
            return (valid_num*number)
                
                
    return 0
            
print(get_numbers(2020,liste,2))

print(get_numbers(2020,liste,3))
            
