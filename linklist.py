# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 19:16:14 2023

@author: msi
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion at the end of the list
    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Deletion of a specific value from the list
    def remove(self, value):
        if not self.head:
            return

        if self.head.data == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next and current.next.data != value:
                current = current.next
            if current.next:
                current.next = current.next.next

    # Searching for a specific value in the list
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    # Display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Sample usage:
if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    # Declare a pre-defined list of elements
    elements_list = [12, 5, 23, 8, 19]

    # Insert elements from the list into the linked list
    for value in elements_list:
        linked_list.insert(value)
        linked_list.display()

    value_to_insert = int(input("Enter value to insert: "))
    linked_list.insert(value_to_insert)
    linked_list.display()

    value_to_remove = int(input("Enter value to remove: "))
    linked_list.remove(value_to_remove)
    linked_list.display()

    value_to_search = int(input("Enter value to search: "))
    if linked_list.search(value_to_search):
        print("Value found in the linked list.")
    else:
        print("Value not found in the linked list.")
