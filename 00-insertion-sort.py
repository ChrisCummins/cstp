#!/usr/bin/env python
#
## The insertion sort:
#
# Accepts an array of objects 'data' {d1,d2,...dn} and returns a permutation of
# the input sequence such that {d'1<=d'2<=...<=d'n}. The 'compare_func' is a
# lambda function which compares two elements from within the data set and
# returns 1, 0 or -1 depending on whether the value of the first key is greater,
# equal, or lesser than that of the second key.
#
# The insertion sort is an efficient algorithm for sorting a small number of
# elements. Insertion sort works by maintaining an ordered and an unordered
# subarray. At the start, all the elements are in the unordered subarray. One by
# one, an element is taken from the unordered subarray and inserted into the
# sorted subarray by comparing the current key against each key in the unordered
# subarray from right to left. This process is repeated until their are no items
# left in the unordered subarray.
#
## Performance:
#
# Worst case performance:   O(n^2)
# Best case performance:    O(n)
# Average case performance: O(n^2)
# Actual performance:       O(n+d), where d is the number of inversions
# Memory usage:             O(1), in-place
#
## Advantages:
#
# Efficient for small data sets.
# Efficient for data sets that are already largely sorted.
# More efficient in practice than other simple quadratic algorithms
#  (e.g. selection sort, bubble sort).
# Stable - does not change the relative order of elements with equal keys.
# In-place - only requires a constant amount O(1) of additional memory.
# Online - can sort a list as it receives it.
#
## References:
#
# Introduction to Algorithms, section 2.1, page 16.
#
## Code:
#
import lib

def insertion_sort(data):
    for j in range(1, len(data)):
        key = data[j]
        # Insert data[j] into sorted sequence data[0..j-1].
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i + 1] = data[i]
            i = i - 1
            data[i + 1] = key

    return data

if __name__ == "__main__":
    lib.test_array_sort(insertion_sort)
