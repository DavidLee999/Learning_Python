# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:55:19 2017

@author: li_pe
"""

from multiprocessing import Process, Queue
import time, random

def write(q):
    
    for value in ['A','B','C']:
        
        print 'Put %s to queue ...' %value
        
        q.put(value)
        
        time.sleep( random.random() )

def read(q):
    
    while True:
        
        value = q.get(True)
        
        print 'Get %s from queue.' % value
        
if __name__ == '__main__':
    
    q = Queue()
    
    pw = Process( target=write, args=(q,) )
    pr = Process( target=read, args=(q,) )
    
    pw.start()
    pr.start()
    
    pw.join()
    
    pr.terminate()