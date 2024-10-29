# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:31:05 2023

@author: DELL
"""

def selection_sort(A):
    
    N = len(A) 
    for i in range(0,N):
        min = i
        for j in range(i+1,N):
           
          if A[j] < A[min]:
              min = j
              
        tmp = A[i]
        A[i] = A[min]
        A[min] = tmp
          
             
            
            
A = [3,9,6,1,2]
selection_sort(A)
print("Sorted List ",A)            