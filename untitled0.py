# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 11:45:19 2017

@author: li_pe
"""

def name_standardized(name):
    
    #return name[0].upper() + name[1:].lower()
   return name.capitalize()


print map(name_standardized, ['adam', 'LISA', 'barT'])