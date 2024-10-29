# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 09:29:34 2023

@author: DELL
"""

class Node:
    def __init__(self,data):   #1st class -node create
       self.data = data
       self.next = None
       
class Linkedlist:
    def __init__(self):
       self.head = None    #2nd class -link list craete
       
    def traverse(self,head):
        while head != None:
            print(head.data)
            head = head.next
    def delete_by_loc(self,head,pos):
       prev = head
       c = 1
       while prev.next.next != None:
           if c == pos-1:
               break
           else:
               prev = prev.next
               c+=1
       cur = prev.next
       #print(cur.data)
       prev.next = cur.next        
       
first = Node(10)
second = Node(20)
third = Node(30)
newNode = Node(40)
endNode = Node(50)
midNode = Node(100)



L = Linkedlist()
L.head = first
first.next = second
second.next  = third 
 
#temp = L.head
newNode.next = L.head
L.head = newNode

#end node
third.next = endNode



#middle node
t = L.head
while t != None:
    if t.data == 20:
        break
    else:
        t = t.next
midNode.next = t.next
t.next = midNode 

 
#count nodes
c = 1
t1 = L.head
while c != 4:
    t1 = t1.next
    c = c + 1
t1.data = 80   

#delete from beginning
L.head = newNode.next 

#delete from end
t2 = L.head
while t2.next.next != None:
    t2 = t2.next
t2.next = None

#delete by value
prev = L.head
flag = 0
while prev.next.next !=None:
    if prev.next.data == 80:
        flag = 1
        break
    else:
        prev = prev.next
cur = prev.next
if flag == 1:
  prev.next = cur.next
  #update
  #cur.data= 100
else:
    print("Deletion not possible!")
    
    
L.delete_by_loc(L.head,2)   
#print linkedlist
temp = L.head
L.traverse(temp)    
      


#print linkedlist
#temp = L.head
#L.traverse(temp)