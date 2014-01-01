#!/usr/bin/env python
#
## The merge sort:
#
# Accepts an array of objects 'data' {d1,d2,...dn} and returns a permutation of
# the input sequence such that {d'1<=d'2<=...<=d'n}.
#
# The merge sort is a divide and conquer algorithm. It works by
# dividing the unsorted array into n arrays, each containing 1
# element, then repeatedly merging arrays to produce new sorted arrays
# until there is only 1 array remaining. Merge sorting is stable, that
# is that the input order of equal elements is preserved.
#
## Performance:
#
# Worst case performance:       O(n log n)
# Best case performance:        O(n log n)
# Average case performance:     O(n log n)
# Memory usage:                 O(n), but can be in-place
#
## Advantages:
#
# Much more efficient on larger datasets than insertion sort.
# Efficient at handling slow-to-access sequential media (used in tape drives).
# Both Perl and Java use merge sort as their default sorting algorithms.
# Python uses timsort, a tuned hybrid of merge sort.
#
## Disadvantages:
#
# Has an increased memory footprint over the in place O(1) heapsort.
#
## References:
#
# Introduction to Algorithms, section 2.3.1, page 31.
# http://stackoverflow.com/questions/18761766/mergesort-python
# http://en.wikipedia.org/wiki/Merge_sort
#
## Code:
#
def merge_sort(data):

    # Receives two lists as arguments, and returns a sorted list
    # of both.
    def merge(left, right):
        result = []

        while (len(left) > 0) or (len(right) > 0):
            if len(left) > 0 and len(right) > 0:
                if left[0] > right[0]:
                    result.append(right[0])
                    right.pop(0)
                else:
                    result.append(left[0])
                    left.pop(0)
            elif len(right) > 0:
                for i in right:
                    result.append(i)
                    right.pop(0)
            else:
                for i in left:
                    result.append(i)
                    left.pop(0)

        return result

    # A list of 1 element or an empty list is considered sorted.
    if len(data) <= 1:
        return data

    middle = int(len(data)/2)
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])

    return merge(left, right)

if __name__ == "__main__":
    # Simple test
    a = [31, 41, 59, 26, 41, 58]
    print "Unsorted:", a
    b = merge_sort(a)
    print "Sorted:  ", b
