# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 09:19:08 2017

@author: li_pe
"""

' a test module'

__author__  = 'Li'

import sys

def test():
    
    args = sys.argv
    
    if len(args) == 1:
        
        print 'Hello, world.'
        
    elif len(args) == 2:
        
        print 'Hello, %s.' % args[1]
        
    else:
        
        print 'too much arguments.'
        
if __name__ == '__main__':
    
    test()