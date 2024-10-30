# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 05:10:15 2023

@author: msi
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion at a specific position in the list
    def insert(self, value, position):
        new_node = Node(value)
        if position == 0:  # Insert at the beginning
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 0
            while current and count < position - 1:
                current = current.next
                count += 1
            if current:
                new_node.next = current.next
                current.next = new_node
            else:  # If position is greater than the length of the list, append at the end
                self.insert_at_end(value)

    # Insertion at the end of the list
    def insert_at_end(self, value):
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
        position = 0
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1

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

    # Take elements list as input from the user
    elements_list = [int(x) for x in input("Enter elements separated by spaces: ").split()]

    # Insert elements from the list into the linked list at the end
    for value in elements_list:
        linked_list.insert_at_end(value)
        linked_list.display()

    value_to_insert = int(input("Enter value to insert: "))
    position_to_insert = int(input("Enter position to insert (0-indexed): "))
    linked_list.insert(value_to_insert, position_to_insert)
    linked_list.display()

    value_to_remove = int(input("Enter value to remove: "))
    linked_list.remove(value_to_remove)
    linked_list.display()

    value_to_search = int(input("Enter value to search: "))
    position_found = linked_list.search(value_to_search)
    if position_found != -1:
        print(f"Value found at position {position_found} in the linked list.")
    else:
        print("Value not found in the linked list.")
