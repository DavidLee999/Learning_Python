# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 16:16:43 2017

@author: li_pe
"""

import functools

def log(text):
    
    if type(text) == type(log):
        
        @functools.wraps(text)
        
        def new_now(*args, **kw):
            
            print 'call %s(): ' % text.__name__
              
            return text(*args, **kw)
        
        return new_now
    
    else:
        
        def decorate(func):
        
            @functools.wraps(func)
        
            def new_now(*args, **kw):
            
                print 'begin call.'
            
                print '%s %s(): ' % (text, func.__name__)
            
                print 'end call.'
            
                return func(*args, **kw)
        
            return new_now
        
        return decorate


@log#('exercute')

def now():
    
    print '06.06.2017'
    

now()