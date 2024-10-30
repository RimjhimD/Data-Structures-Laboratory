# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 01:32:26 2023

@author: msi
"""

def selection_sort(A):
    N = len(A)
    for i in range(0,N):
        min_index = i
        for j in range(i+1,N):
            
            if A[j]<A[min_index]:
                min_index = j
                
        tmp = A[i] 
        A[i] = A[min_index]
        A[min_index] = tmp
         
A=input("Enter a list of numbers separated by space:").split()  
A=[int (num) for num in A]

selection_sort(A)
print("Sorted list: ",A)         
                
            
        