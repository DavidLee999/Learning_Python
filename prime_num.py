# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 12:11:53 2017

@author: li_pe
"""

def prime_num(num):
    
    for i in range(2, int(num/2 + 1)):
        
        if num % i == 0:
            
            return 1
        
    else:
            
        return 0
    
print filter(prime_num, range(2,101))

