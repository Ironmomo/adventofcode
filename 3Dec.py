# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:52:30 2020

@author: andri
"""
#You start on the open square (.) in the top-left corner and need to reach the bottom 
#The toboggan can only follow a few specific slopes 
#start by counting all the trees you would encounter for the slope right 3, down 1:
#From your starting position at the top-left, check the position that is right 3 and down 1. 
#Then, check the position that is right 3 and down 1 from there, and so on 
#until you go past the bottom of the map.

file = open("3Dec.txt","r")
x = 0
trees = 0

for line in file:
    if line[x%31] == "#":
        trees += 1
    x += 3

print(trees)

file.close()

######################################################
  ####################Part Two######################
######################################################
#my solution got a bit messed up but in the end it showed the right number so...


slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)] #(right,down)

def file_to_list():
    file = open("3Dec.txt","r")
    liste = []
    for line in file:
        line = line.split()
        for char in line:
            liste.append(char)
        
    file.close()    
    return liste

def get_trees(liste,slopes):
    res = 1
    for slope in slopes:
        x = 0
        y = 0
        trees2 = 0
        
        for line in range(int(len(liste)/slope[1])):
            
            if liste[y][x%31] == "#":
                trees2 += 1
            x += slope[0]
            y += slope[1]
    
        res = res*trees2
        
    print(res)


liste = file_to_list()

get_trees(liste,slopes)
