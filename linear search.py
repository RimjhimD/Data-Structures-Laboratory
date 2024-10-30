# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 22:21:22 2023

@author: msi
"""

def linear_search(A,ITEM):
    for i in range(len(A)):
        if A[i]==ITEM:
            return i
    return - 1


A=[10,20,30,50,90]
ITEM = 50
result = linear_search(A,ITEM)
if result == -1:
   print("Element not found")
else:
   print("Element found at index:",result)    
        