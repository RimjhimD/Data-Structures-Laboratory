# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 09:58:07 2023

@author: DELL
"""

class Node:
    def __init__(self,data):   #1st class -node create
       self.data = data
       self.next = None
       
class CLinkedlist:
    def __init__(self):
       self.head = None    #2nd class -link list craete
       
    def traverse(self,head):
        print(head.data)
        temp = head.next
        while temp != head:
            print(temp.data)
            temp = temp.next
       
first = Node(10)
second = Node(20)
third = Node(30)



L = CLinkedlist()
L.head = first
first.next = second
second.next  = third 
third.next = L.head

L.traverse(L.head)
 