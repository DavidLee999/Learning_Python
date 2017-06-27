# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:55:19 2017

@author: li_pe
"""

from multiprocessing import Process, Pipe
import time, random

def sendmsg( conn ):
    
    for value in ['A', 'B', 'C', 'D']:
        
        print 'Send %s to Pipe' % value
        
        conn.send( value )
        
        time.sleep( random.random() )
        
def recvmsg( conn ):
    
    while True:
        
        value = conn.recv()
        
        print 'Recv %s from Pipe' % value
        
if __name__ == '__main__':
    
    conn1, conn2 = Pipe()
    ps = Process( target = sendmsg, args = (conn1,) )
    pr = Process( target = recvmsg, args = (conn2,) )
    
    ps.start()
    pr.start()
    
    ps.join()
    
    pr.terminate()