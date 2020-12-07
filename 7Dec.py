# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:56:45 2020

@author: andri
"""

import re

with open("7Dec.txt") as file:
    rules = file.read().split("\n")
    


pattern ="([a-z]+ [a-z]+) bags"
pattern2 = "(\d)+ ([a-z]+ [a-z]+)"

valid = []
graph = {}


for i in rules:

    r = re.match(pattern, i)
    color_sec = re.findall(pattern2,i)
    color_prim = r.group(1)
 
    for color in color_sec:
        
        if "shiny gold" == color[1]:
            valid.append(color_prim)

    if len(color_sec) > 0:
        #c = list(zip(*color_sec))
        #graph[color_prim] = c[1]
        graph[color_prim] = color_sec


                
def shiny_gold(color):

    if color == "shiny gold":
        return True
    
    else:
        return any(shiny_gold(colors[1]) for colors in graph.get(color,[]))


print("Part one:",sum(shiny_gold(color) for color in graph.keys())-1)

def count(color):
    if color == "":
        return 1
    return 1 + sum(int(amount)*count(child) for amount, child in graph.get(color,[]))
print(count("shiny gold")-1)




