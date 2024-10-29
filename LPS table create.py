# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 10:15:11 2023

@author: DELL
"""

def lps_table(pat):
    
    M = len(pat)
    lps = [0]*M
    i = 0
    j = 1
    lps[0]=0
    while j<M:
        if pat[i] == pat[j]:
            lps[j] = i+1
            i+=1
            j+=1
            
        else:
            if i == 0:
                lps[j] = 0
                j += 1
                
            else:
                i = lps[i - 1]
                
    print(lps)  
    
    
    
    
    
pat = "ABCDABD"
lps_table(pat)       