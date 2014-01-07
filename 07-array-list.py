#!/usr/bin/env python
#
## Array Lists:
#
# A random access, variable-size list data structure. A common way of
# implementing this is to double the size of the array when it reaches
# capacity, and to copy the existing values into the new array.
#
## Performance:
#
# Indexing:                     O(1)
# Insert:                       O(1), or O(n) when at capacity
# Wasted space:                 0(n)
#
## References:
#
# http://en.wikipedia.org/wiki/Dynamic_array
#
## Code:
#
class ArrayList:

    def __init__(self, starting_capacity=1):
        self.list = [None] * starting_capacity
        self.size = 0
        self.capacity = starting_capacity

    def append(self, x):
        if self.size == self.capacity:
            new_capacity = self.capacity * 2
            new_list = [None] * new_capacity

            # Copy data into new array:
            for i in range(self.size):
                new_list[i] = self.list[i]

            self.list = new_list
            self.capacity = new_capacity

        self.list[self.size] = x
        self.size = self.size + 1

    def get(self, index):
        if index > 0 and index < self.size:
            return self.list[index]

    def __str__(self):
        if self.size:
            return str(self.list[:self.size])

if __name__ == "__main__":
    a = ArrayList()

    for i in range(10000):
        a.append(i)
