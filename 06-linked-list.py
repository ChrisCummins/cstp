#!/usr/bin/env python
#
## Linked Lists:
#
# A linked list is a data structure in which the objects are arranged
# in a linear order. The order in a linked list is determined by a
# pointer in each object.
#
## Performance:
#                   Singly-linked  |  Doubly-linked
#                  Unsorted Sorted | Unsorted Sorted
# SEARCH(L,k)      O(n)     O(n)   | O(n)     O(n)
# INSERT(L,x)      O(1)     O(n)   | O(1)     O(n)
# DELETE(L,x)      O(n)     O(n)   | O(n)     O(n)
# SUCCESSOR(L,x)   O(1)     O(1)   | O(1)     O(1)
# PREDECESSOR(L,x) O(n)     O(n)   | O(1)     O(1)
# MINIMUM(L)       O(n)     O(1)   | O(n)     O(1)
# MAXIMUM(L)       O(n)     O(n)   | O(n)     O(1)
#
## Advantages:
#
# TODO: bullet point list of advantages
#
## Disadvantages:
#
# TODO: bullet point list of disadvantages
#
## References:
#
# Introduction to Algorithms, section 10.2, page 236.
#
## Code:
#
import lib

class Element:

    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

    def __repr__(self):
        return repr(self.key)

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def insert(self, x):
        x.next = self.head
        self.head = x

    def delete(self, x):
        prev = self.predecessor(x)
        if prev:
            prev.next = x.next
        else:
            self.head = x.next

    def get(self, index):
        i = 0
        x = self.head
        while x and i != index:
            x = x.next
            i = i + 1
        return x

    def search(self, key):
        x = self.head
        while x and x.key != key:
            x = x.next
        return x

    def successor(self, x):
        return x.next

    def predecessor(self, x):
        y = self.head
        z = None

        while y and y != x:
            z = y
            y = y.next

        return z

    def minimum(self):
        min = self.head
        x = self.head

        while x:
            if x.key < min.key:
                min = x
            x = x.next

        return min

    def maximum(self):
        max = self.head
        x = self.head

        while x:
            if x.key > max.key:
                max = x
            x = x.next

        return max

    def __str__(self):
        s = ""
        x = self.head
        while x:
            s += repr(x) + " "
            x = x.next
        return s

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insert(self, x):
        x.next = self.head
        x.prev = None
        if self.head:
            self.head.prev = x
        self.head = x

    def delete(self, x):
        if x.prev:
            x.prev.next = x.next
        else:
            self.head = x.next

        if x.next:
            x.next.prev = x.prev

    def get(self, index):
        i = 0
        x = self.head
        while x and i != index:
            x = x.next
            i = i + 1
        return x

    def search(self, key):
        x = self.head
        while x and x.key != key:
            x = x.next
        return x

    def successor(self, x):
        return x.next

    def predecessor(self, x):
        return x.prev

    def minimum(self):
        min = self.head
        x = self.head

        while x:
            if x.key < min.key:
                min = x
            x = x.next

        return min

    def maximum(self):
        max = self.head
        x = self.head

        while x:
            if x.key > max.key:
                max = x
            x = x.next

        return max

    def __str__(self):
        s = ""
        x = self.head
        while x:
            s += repr(x) + " "
            x = x.next
        return s

if __name__ == "__main__":

    print "UNSORTED SINGLY LINKED LIST:"
    lib.test_linked_list(SinglyLinkedList(), Element)

    print "UNSORTED DOUBLY LINKED LIST:"
    lib.test_linked_list(DoublyLinkedList(), Element)
