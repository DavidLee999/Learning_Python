# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def str2int(s):
    
    def char2int(c):
        
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[c]
    
    def add(x, y):
        
        return x*10 + y
    
    return reduce(add, map(char2int, s))