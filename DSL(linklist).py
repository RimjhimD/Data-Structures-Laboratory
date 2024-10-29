# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 08:28:27 2023

@author: DELL
"""

class Student:
    
    def __init__(self,id,name):
        self.student_id = id
        self.name = name
        
    def student__info(self):
        print("Student ID"+str(self.student_id)+" and Student Name: "+self.name)
        
    def student__result(self):
        print("Student Result")
        
student1 = Student(1234,'AB')
student2 = Student(5678,'CD')
print(student1.student__info())
print(student2.student__info())       
        