# -*- coding: utf-8 -*-
"""
Created on Wed May 31 10:24:03 2017

@author: li_pe
"""

def triangles(max):
    
    L = [1]
      
    j = 0
    
    L_ex = L 
    while j < max:
        yield L
        if len(L) < 2:
            L.append(1)
        else:
            L = [1]
            n = 1
            while n < len(L_ex):
                L.append(L_ex[n-1]+L_ex[n])
                n = n + 1
            L.append(1)
        L_ex = L        
        
        


               
for t in triangles(10):
    
    print t
     