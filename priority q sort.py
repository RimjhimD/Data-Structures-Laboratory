# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:11:22 2023

@author: DELL
"""

def Prioqueue(Q,val):
    Q.append(val)
    Q.sort(reverse=True)
    
    

        
Q = []        

Prioqueue(Q,(1,'A'))
Prioqueue(Q,(2,'C'))
Prioqueue(Q,(3,'D'))
Prioqueue(Q,(4,'B'))  

while Q:
    print(Q.pop(0))