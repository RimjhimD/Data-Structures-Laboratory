# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 08:48:08 2023

@author: DELL
"""

def pattern_match(txt,pat):
    
    M = len(txt)
    N = len(pat)
    
    for i in range(M-N+1):
        for j in range(N):
            if txt [i+j] != pat[j]:
                break
            if (j == N-1):
                print("Pattern found at loc:",i)
                
txt = "ABCDABCDAB"
pat = "DAB" 
pattern_match(txt,pat)               