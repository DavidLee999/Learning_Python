# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 15:34:46 2017

@author: li_pe
"""

def count1():
    
    fs = []
    
    for i in range(1, 4):
        
        def f():
            
            return i * i
        
        fs.append(f)
    
    return fs

def count2():
    
    fs = []
    
    for i in range(1, 4):
        
        def f(j):
            
            def g():
                
                return j * j
            
            return g
        
        fs.append(f(i))
    
    return fs

f1, f2, f3 = count1()

f4, f5, f6 = count2()

print f1(), f2(), f3()

print f4(), f5(), f6()