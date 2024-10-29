# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:34:26 2023

@author: DELL
"""
def search(text,pat):
         
         N = len(text)
         M = len(pat)
         
         for i in range(N-M+1):
             for j in range(M):
                 if txt[i+j] != pat[j]:
                     break
                 
                 if j == M-1:
                     print("pattern found at loc: ",i)
                     
                     
txt = "ABCDADRTCDA"
pat = "CDA" 
search(txt,pat)              
             
             
           