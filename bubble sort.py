# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 23:38:18 2023

@author: msi
"""

def bubble_sort(lst):
    N = len(lst)
    for i in range(0,N):
      for j in range(1,N-i):
          
          if lst[j-1] > lst[j]:
             tmp = lst[j-1]
             lst[j-1] = lst[j]
             lst[j] = tmp
          
numbers=input("Enter a list of numbers separated by space:").split()  
lst=[int (num) for num in numbers]

bubble_sort(lst)
print("Sorted list: ",lst)

         