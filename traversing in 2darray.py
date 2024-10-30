# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 21:06:08 2023

@author: msi
"""

def traversal(arr):
   rows = len(arr)
   columns = len(arr[0])
   
   for i in range(rows):
       for j in range(columns):
           print(arr[i][j],end = ' ')
           
arr=[ 
      [1,2,3],
      [4,5,6],
      [7,8,9] ]
traversal(arr)           