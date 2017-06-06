# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 11:45:19 2017

@author: li_pe
"""

def name_standardized(name):
    
    new_name1 = name[1:].lower()
    
    new_name0 = name[0].upper()
    
    new_name = new_name0 + new_name1
    
    print new_name
   
name_standardized('mIKE')