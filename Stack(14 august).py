# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 09:48:45 2023

@author: DELL
"""
def push(val,S):
    S.append(val)
  
    
def pop(S):
    N = len(S)
    if N == 0:
        print("Stack is empty!")
        
    else:
        return S.pop()

def infix_to_postfix(S,string):
    op = ['+','-','*','/','(',')']
    P = {'+':1,'-':1,'*':2,'/':2}
    B = ['(',')']
    exp = ''
    for c in string:
        if c not in op and c not in B:
            exp = exp + c
        elif c == '(':
            push(c,S)
        elif c == ')':
            while S  and S[-1] != '(':
                exp = exp + pop(S)
            pop(S)    
            
            
        else:
            while S and S[-1] != '(' and P[c] < P[S[-1]]:
                exp = exp + pop(S)
            push(c,S)
            
    while S:
         exp = exp + pop(S)
    print(evaluate_postfix(S,exp)) 

def evaluate_postfix(S,string):
    op = ['+','-','*','/']
    for i in string:
        if i not in op:
            push(i,S)
        else:
            a = pop(S)
            b = pop(S)
            if i == '+':
                res = int(a)+int(b)
                push(res,S)
            if i == '-':
                res = int(a)-int(b)
                push(res,S)
            if i == '*':
                res = int(a)*int(b)
                push(res,S)
            if i == '/':
                res = int(a)/int(b)
                push(res,S)                
    return S    
          
    #print(exp)
          
stack = []
string = "6+(5*9)" 
infix_to_postfix(stack,string)         
          