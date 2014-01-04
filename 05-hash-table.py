#!/usr/bin/env python
#
## Hash Tables:
#
# An associate array that maps keys to values, by using a hash
# function to generate an index into the array of buckets, from which
# the correct value can be found.
#
## Performance:
#
# Worst case performance:       O(n)
# Best case performance:        O(1)
# Average case performance:     O(1)
# Memory usage:                 O(n)
#
## Advantages:
#
# Turns O(n) lookup into O(1).
#
## Disadvantages:
#
# Performance depends largely on the quality of the hash function and
#  the number of buckets available. Will degrade from O(1) to O(n).
#
## References:
#
# https://sites.google.com/site/usfcomputerscience/hash-tables-imp
# http://en.wikipedia.org/wiki/Hash_table
#
## Code:
#
import lib

class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value

# An example of a very naive implementation. This just adds key value
# pairs into a list. Retrieval of elements involves just brute forcing
# through the list, so is O(n). There's no buckets, so there's no
# collision handling.
class BadHashTable:
    def __init__(self, size=20):
        self.list = [None] * size

    def set(self, key, value):
        self.list.append(KeyValue(key, value))

    def get(self, key):
        for entry in self.list:
            if entry and entry.key == key:
                return entry.value

# A proper hash table. The (primitive) hash function just casts the
# key to a string, then sums up the ASCII values of all the
# characters. This implementation offers collision avoidance by using
# list buckets.
class HashTable:
    def __init__(self, size=20):
        self.list = [list()] * size

    def hash(self, key):
        total = 0
        for c in str(key):
            total = total + ord(c)
        return total % len(self.list)

    def set(self, key, value):
        index = self.hash(key)
        entry = KeyValue(key, value)
        self.list[index].append(entry)

    def get(self, key):
        index = self.hash(key)
        for entry in self.list[index]:
            if entry.key == key:
                return entry.value

if __name__ == "__main__":
    print "Good Hash Table:"
    lib.test_hash_table(HashTable)
    print "\nBad Hash Table:"
    lib.test_hash_table(BadHashTable)
