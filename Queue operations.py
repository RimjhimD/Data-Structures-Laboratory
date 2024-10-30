# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 14:36:55 2023

@author: msi
"""

size = 5

def Enqueue(Q, val):
    if len(Q) == size:
        print('Overflow! Queue is full!')
        return
    else:
        Q.append(val)
        print('After Enqueue operation:', Q)

def Dequeue(Q):
    if not Q:
        print('Underflow! Queue is empty!')
        return
    else:
        item = Q.pop(0)
        print('Deleted item:', item)
        print('After Dequeue:', Q)

# Sample input and output for Enqueue and Dequeue
Q = []
Enqueue(Q, 5)
Enqueue(Q, 10)
Enqueue(Q, 15)
Enqueue(Q, 20)
Enqueue(Q, 25)
Enqueue(Q, 30)
Dequeue(Q)
size = size - 1
Dequeue(Q)
size = size - 1
Dequeue(Q)
size = size - 1
Enqueue(Q, 35)

def Prioqueue(Q, val):
    Q.append(val)
    Q.sort(reverse=True)

# Sample input and output for Priority Queue
Q = []
Prioqueue(Q, (1, 'A'))
Prioqueue(Q, (2, 'C'))
Prioqueue(Q, (3, 'D'))
Prioqueue(Q, (4, 'B'))

def D_prQ(Q):
    if len(Q) == 0:
        print("Queue is empty!")
    else:
        Q.pop(0)
        print('After deletion:', Q)

# Sample input and output for Dequeue from Priority Queue
D_prQ(Q)

Prioqueue(Q, (5, 'E'))

while Q:
    print(Q.pop(0))