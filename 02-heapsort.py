#!/usr/bin/env python
#
## Heapsort:
#
# Accepts an array of objects 'data' {d1,d2,...dn} and returns a permutation of
# the input sequence such that {d'1<=d'2<=...<=d'n}.
#
# A (binary) heap is an array that can be viewed as a nearly complete
# binary tree, where each node of the tree corresponds to an element
# of the array. The tree is filled on all levels except possible the
# lowest, which is filled from the left up to a point.
#
# Heapsort is a comparison-based sorting algorithm that is split into
# two steps. First, a heap is built out of the data. In the second
# step, a sorted array is created by repeatedly removing the largest
# element from the heap, and inserting it into the array. The heap is
# reconstructed after each removal. Once all objects have been removed
# from the heap, we have a sorted array.
#
## Performance:
#
# Worst case performance:       O(n log n)
# Best case performance:        O(n log n)
# Average case performance:     O(n log n)
# Memory usage:                 O(1)
#
## Advantages:
#
# Has a more favourable worst-case performance than quicksort.
# In-place - only requires a constant amount O(1) of additional memory.
#
## Disadvantages:
#
# Somewhat slower in practice than a well-implemented quicksort.
# Not a stable sort, that is, the order of equal value elements is not
#  preserved.
#
## References:
#
# Introduction to Algorithms, section 6.1, page 151.
# http://www.cs.usfca.edu/~galles/visualization/HeapSort.html
# http://en.wikipedia.org/wiki/Heapsort
#
## Code:
#
def heap_sort(data):

    # Input a heap array and an index into that array. It lets the
    # value at heap[i] "float down" in the max-heap so that the
    # subtree rooted at index i obeys the max-heap property.
    def max_heapify(heap, heap_size, i):

        # Helper functions to get the relative nodes of a specific
        # index.
        #
        # Note that these can be implemented in single instructions by
        # shifting the bits:
        #
        #   PARENT(i): return i >> 1
        #   LEFT(i):   return i << 1
        #   RIGHT(i):  return (i << 1) + 1
        #
        # Note also that the parent_index function is not needed for
        # the heap_sort implementation, it is included here for
        # completeness.
        #
        def parent_index(i):
            return i / 2

        def left_index(i):
            return 2 * i

        def right_index(i):
            return 2 * i + 1

        left = left_index(i)
        right = right_index(i)

        if left < heap_size and heap[left] > heap[i]:
            largest = left
        else:
            largest = i

        if right < heap_size and heap[right] > heap[largest]:
            largest = right

        if largest != i:
            heap[i], heap[largest] = heap[largest], heap[i]
            max_heapify(heap, heap_size, largest)

    # Input an array and build into a max heap.
    def build_max_heap(data):
        for i in range(len(data) / 2 - 1, -1, -1):
            max_heapify(data, len(data), i)

    # The first step: build the entire array into a max heap.
    build_max_heap(data)

    # The second step: Continuously remove the largest object from the
    # heap, and rebuild the max heap. Continue until there are no
    # objects left in the heap.
    for i in range(len(data) - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        max_heapify(data, i, 0)

    return data

if __name__ == "__main__":
    # Simple test
    a = [31, 41, 59, 26, 41, 58]
    print "Unsorted:", a
    heap_sort(a)
    print "Sorted:  ", a
    assert a == [26, 31, 41, 41, 58, 59]
