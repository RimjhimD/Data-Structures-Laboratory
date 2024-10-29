# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:52:35 2023

@author: DELL
"""

class T:
    
    def __init__(self,data):
        self.data = data
        self.left_child = 10
        self.right_child = 25
        
        
    def print_T(self):
        print(self.data)
        #print(self.left_child)
        #print(self.right_child)
        if self.left_child:
            self.left_child.print_T()
        if self.right_child:
            self.right_child.print_T()
        
    def insert_T(self,val):
        if self.data:
            if val < self.data:
                if self.left_child:
                    self.left_child.insert_T(val)
                else:
                    self.left.child = T(val)
            elif val > self.data:
                if self.right_child:
                    self.right_child.insert_T(val)
                else:
                    self.right_child = T(val)
                    
        else:
             self.data = val
        
root = T(20)

root.insert_T(5)
root.insert_T(25)
root.insert_T(2)
root.insert_T(10)
root.insert_T(22)
root.insert_T(30)

#root.print_T()   











     