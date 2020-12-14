# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:42:02 2020

@author: andri
"""
with open("8Dec.txt") as f:
    boot_sequence = f.read().splitlines()

def part_one(boot_sequence):
    idx = 0
    acc = 0
    operation = boot_sequence[idx]
    check_op = [False for c in boot_sequence]
    
    while True:
        
        check_op[idx] = True
        op, value = operation.split()
        
        if op == "acc":
            acc += int(value)
            idx += 1
            
        elif op == "jmp":
            idx += int(value)
            
        elif op == "nop":
            idx += 1
            
        if check_op[idx] == True:
            break
        
        operation = boot_sequence[idx]
        
    print(acc)
        
def part_two(boot_sequence):
    
    for o in range(len(boot_sequence)):
        boot_copy = []
        for c in boot_sequence:
            boot_copy.append(c)
            
        if boot_copy[o].split()[0] == "jmp":
            boot_copy[o] = boot_copy[o].replace("jmp","nop")
        elif boot_copy[o].split()[0] == "nop":
            boot_copy[o] = boot_copy[o].replace("nop","jmp")
            
            
        idx = 0
        acc = 0
        operation = boot_copy[idx]
        check_op = [False for c in boot_copy]
        
        while True:
            check_op[idx] = True
            op, value = operation.split()
            
            if op == "acc":
                acc += int(value)
                idx += 1
                
            elif op == "jmp":
                idx += int(value)
                
            elif op == "nop":
                idx += 1

            if idx == len(boot_copy):
                print(acc)
                break
                
            elif check_op[idx] == True:
                break

            else:
                operation = boot_copy[idx]
            

part_one(boot_sequence)
part_two(boot_sequence)