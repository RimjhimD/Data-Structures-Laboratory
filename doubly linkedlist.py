# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:19:02 2023

@author: DELL
"""

class Node:
    def __init__(self,data):   #1st class -node create
       self.data = data
       self.next = None
       self.prev = None
       
class DLinkedlist:
    def __init__(self):
       self.head = None     #2nd class -link list craete
       
    def traverse(self,head):
        while head != None:
            print(head.data)
            head = head.next
       
first = Node(10)
second = Node(20)
third = Node(30)



L = DLinkedlist()
L.head = first
first.next = second
second.next  = third 
second.prev = first
third.prev = second

L.traverse(L.head)
 