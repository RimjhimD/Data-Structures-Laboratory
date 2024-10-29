# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 10:18:23 2023

@author: DELL
"""
size = 5
def Enqueue(Q,val):
    if len(Q) == size:
        print('Overflow! Queue is full!')
        return
    else:
        Q.append(val)
        print('After Enqueue operation: ',Q)
        
def Dequeue(Q):
    if not Q:
        print('Underflow! Queue is empty!')
        return
    else:
        item = Q.pop(0)
        print('Deleted item: ',item)
        print('After Dequeue: ',Q)        

Q = []
Enqueue(Q,5)
Enqueue(Q,10)
Enqueue(Q,15)
Enqueue(Q,20) 
Enqueue(Q,25) 
Enqueue(Q,30)
Dequeue(Q)
size = size - 1
Dequeue(Q)
size = size - 1
Dequeue(Q)
size = size - 1
Enqueue(Q,35)         
    
    