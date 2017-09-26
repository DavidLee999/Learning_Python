# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 12:05:46 2017

@author: li_pe
"""

def prod(argu):
    
    def multi(x, y):
        
        return x * y
    
    return reduce(multi, argu)

print prod([1,2,3,4,5])
