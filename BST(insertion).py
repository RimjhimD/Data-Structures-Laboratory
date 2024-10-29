# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 08:58:04 2023

Rim: DELL
"""

class T:
    
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None
        
def insert_BST(root,val):
   if root is None:
        return T(val)
   else:
       if val < root.data:
           root.left_child = insert_BST(root.left_child,val)
       else:
           root.right_child = insert_BST(root.right_child,val)
   return root

def in_order(root):
    if root:
        in_order(root.left_child)
        print(root.data,end=' ')
        in_order(root.right_child)
        
def pre_order(root):
    if root:
        print(root.data,end=' ')
        pre_order(root.left_child)
        pre_order(root.right_child)
    



def post_order(root):
    if root:
       post_order(root.left_child)
       post_order(root.right_child)
       print(root.data,end=' ') 


def height(root):
    if root is None:
        return 0
    else:
        A = height(root.left_child)
        B = height(root.right_child)
        R = max(A,B) + 1
        
    return  R 

    
    
def full_binary_tree(root):
     if root is None: 
       return True 
     elif root.left_child is None and root.right_child is None:
       return True
     elif root.left_child is not None and root.right_child is not None:
       return(full_binary_tree(root.left_child) and full_binary_tree(root.right_child))   
       
     return False
        
        
root = T(10)        
insert_BST(root,8)
insert_BST(root,15)
insert_BST(root,25)
insert_BST(root,5)

print("\nInorder traversal: ")
in_order(root)
print()
print("\nPreorder traversal: ")
pre_order(root)
print()
print("\nPostorder traversal: ")
post_order(root)

print("\nheight of tree: ",height(root))

if full_binary_tree(root):
    print("\nFull binary tree")
else:
    print("\nNot full binary tree")








             