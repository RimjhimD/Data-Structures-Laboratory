# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 10:12:15 2023

@author: DELL
"""

def insertion_sort(A):
    N = len(A)
    
    for i in range(0,N):
        tmp = A[i]
        j = i
        
        while j>0 and A[j-1]> tmp:
            A[j] = A[j-1]
            j = j-1
            
        A[j] = tmp
        
A=[5,4,3,2,1]
insertion_sort(A)
print("Sorting List ",A)        
        
        
        
        
    