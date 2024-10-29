# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 08:35:38 2023

@author: DELL
"""

def bubble_sort(A):
    N = len(A)
    for i in range(0,N):
        for j in range(1,N-i):
            if A[j-1] > A[j]:
                tmp = A[j-1]
                A[j-1] = A[j]
                A[j] = tmp
                
A = [5,4,1,3,2]
bubble_sort(A)
print("Sorted List: ",A)                
            