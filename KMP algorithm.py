# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:08:44 2023

@author: msi
"""

def lps_table(pat):
    M = len(pat)
    lps = [0] * M
    i = 0
    j = 1
    lps[0] = 0
    while j < M:
        if pat[i] == pat[j]:
            lps[j] = i + 1
            i += 1
            j += 1
        else:
            if i == 0:
                lps[j] = 0
                j += 1
            else:
                i = lps[i - 1]
    return lps

def KMP(txt, pat):
    M = len(pat)
    N = len(txt)
    lps = lps_table(pat)
    i = 0
    j = 0
    while i < N:
        if txt[i] == pat[j]:
            i += 1
            j += 1
        if j == M:
            print("Pattern found at location:", i - j)
            j = lps[j - 1]
        elif i < N and txt[i] != pat[j]:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]

txt = input("Enter the text: ")
pat = input("Enter the pattern: ")
KMP(txt, pat)
