# -*- coding: utf-8 -*-
"""
Created on Fri Jun 02 12:50:35 2017

@author: li_pe
"""

def move(n, a, b, c):
    
    if n == 1:
        
        print ('%s --> %s' %(a, c))
      
    else:
        
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
        
        
move(5,'a', 'b', 'c')