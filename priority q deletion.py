# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 12:52:19 2023

@author: msi
"""

def pr_Q(Q,val):
     Q.append(val)
     Q.sort()
     print('After insertion: ',Q)
     
     
def D_prQ(Q):
    if len(Q) == 0:
        print("Queue is empty!")
    else:
        Q.pop(0)
        print('After deletion: ',Q)
        
        
Q = []

pr_Q(Q,(1,'A'))
pr_Q(Q,(2,'C'))
pr_Q(Q,(3,'D'))
pr_Q(Q,(4,'B'))  

D_prQ(Q)