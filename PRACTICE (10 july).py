# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 21:06:15 2023

@author: msi
"""

def traversal(A,N):
    for i in range(N):
     print(A[i],end=' ')
     
A=[10, 20, 30, 40, 50]
N =len(A)
traversal(A,N)  








def traversal(arr):
   rows = len(arr)
   columns = len(arr[0])
   
   for i in range(rows):
       for j in range(columns):
           print(arr[i][j],end = ' ')
           
arr=[ [1,2,3],
      [4,5,6],
      [7,8,9] ]
traversal(arr)           