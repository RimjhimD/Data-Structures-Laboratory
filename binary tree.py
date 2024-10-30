# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:57:41 2023

@author: msi
"""

class T:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert_BST(self, val):
        if val < self.data:
            if self.left_child:
                self.left_child.insert_BST(val)
            else:
                self.left_child = T(val)
        elif val > self.data:
            if self.right_child:
                self.right_child.insert_BST(val)
            else:
                self.right_child = T(val)

    def in_order(self):
        if self:
            if self.left_child:
                self.left_child.in_order()
            print(self.data, end=' ')
            if self.right_child:
                self.right_child.in_order()


root = T(10)
root.insert_BST(8)
root.insert_BST(15)
root.insert_BST(25)
root.insert_BST(5)

print("Inorder traversal:")
root.in_order()
