# -*- coding: utf-8 -*-
"""
Created on Wed May 31 10:24:03 2017

@author: li_pe
"""

def triangles1(max):
    
    L=[1]
    
    j = 0 
    
    L_ex = L
    
    while j < max:
        
        yield L
        
        j = j + 1
        
        if len(L_ex) < 2:
            
            L.append(1)
            
        else:
            
            L = [1]
            
            n = 1
            
            while n < len(L_ex):
                
                L.append(L_ex[n-1]+L_ex[n])
                
                n = n + 1
                
            L.append(1)
            
        L_ex = L


def triangles2(max): 
    
    L = [1]
    
    j = 0
    
    while j < max:
        
        yield L
        
        L_new = [1]   
        
        for i in range(1,len(L)): 
            
            L_new.append(L[i-1]+L[i])  
                      
        L_new.append(1)
        
        L = L_new  
            
        j = j + 1


def triangles3(max): 
    
    L = [1]
    
    j = 0
    
    while j < max:
        
        yield L  
        
        L = [ L[i-1]+L[i] for i in range(1, len(L))]   
        
        L.insert(0,1) 
                       
        L.append(1) 
             
        j = j + 1


def triangles4(max): 
    L = [1]
    
    j = 0
    
    while j < max:
        
        yield L
        
        L.append(0) 
        
        L = [ L[i-1]+L[i] for i in range(len(L))] 
                     
        j = j + 1
       
        
        


               
for t in triangles1(10):
    
    print t

for t in triangles2(10):
    
    print t
    
for t in triangles3(10):
    
    print t
    
for t in triangles4(10):
    
    print t