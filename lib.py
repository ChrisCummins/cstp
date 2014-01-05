## lib.py - Helper functions for cstp

import random
from time import time

# Input an array and returns true or false depending on whether the
# array was found to be sorted or not. A sorted array is an array
# whereby every element is of equal or greater value than the
# previous.
def array_is_sorted(array):
    for index in range(len(array)):
        next = index + 1

        if next == len(array):
            return True
        elif array[next] < array[index]:
            return False

# Generate an array of random integers of a given length. This method
# guarantees that the return array will be unsorted.
def get_random_int_array(length):
    array = [random.randint(0, 10 * length) for r in xrange(length)]

    if array_is_sorted(array):
        return get_random_int_array(length)

    return array

# Input a sorting algorithm which accepts an array of integers and
# returns a sorted permutation of the array. This function times the
# execution time of the given sorting algorithm across a range of
# input sizes and asserts that the function operates correctly.
def test_array_sort(sort_algorithm):

    for i in range(6):
        test_size = 10 ** (i + 1)

        data = get_random_int_array(test_size)

        t0 = time()
        sorted_data = sort_algorithm(data)
        t1 = time()

        elapsed_time = t1 - t0

        # Confirm that the sort worked
        assert array_is_sorted(sorted_data)

        print "%fs\t%d integers" % (elapsed_time, test_size)

def test_hash_table(hash_table_class):

    for i in range(4):
        test_size = 10 ** (i + 1)
        h = hash_table_class(test_size * 2)

        # Populate table
        for i in range(test_size):
            h.set(i, i * 10)

        # Time the element retrieval
        t0 = time()
        for i in range(test_size):
            assert h.get(i) == i * 10
        t1 = time()
        elapsed_time = t1 - t0

        print ("%f s\t%f s/entry\t%d entries"
               % (elapsed_time, elapsed_time / test_size, test_size))

        # Check that looking up an item which doesn't exist returns nothing
        assert h.get(-1) == None

# Accepts a linked list and element element class, and tests the
# following linked list procedures:
#
#   list.insert(element)
#   list.get(index)
#   list.search(key)
#   list.minimum()
#   list.maximum()
#   list.successor(element)
#   list.predecessor(element)
#   list.delete(element)
#
def test_linked_list(list, element_class):

    for i in range(4):
        test_size = 2 ** (i + 8)
        data = get_random_int_array(test_size)
        data_sorted = sorted(data)
        data_min = min(data_sorted)
        data_max = max(data_sorted)

        # Test INSERT() routine:
        t0 = time()
        for i in data:
            list.insert(element_class(i))
        t1 = time()
        elapsed_time = t1 - t0
        print ("%f s\t%f s/entry\tINSERT()\t%d entries"
               % (elapsed_time, elapsed_time / test_size, test_size))

        # Test SEARCH routine:
        t0 = time()
        for i in data[:test_size / 2]:
            assert list.search(i).key == i
        t1 = time()
        elapsed_time = t1 - t0
        print ("%f s\t%f s/entry\tSEARCH()\t%d entries"
               % (elapsed_time, elapsed_time / test_size, test_size))

        # Check that get operation works:
        t0 = time()
        for i in range(test_size - 1):
            assert list.get(i).key == data[test_size - 1 - i]
        t1 = time()
        elapsed_time = t1 - t0
        print ("%f s\t%f s/entry\tGET()    \t%d entries"
               % (elapsed_time, elapsed_time / test_size, test_size))

        # Check that MINIMUM() works:
        t0 = time()
        for i in range(1000):
            assert list.minimum().key == data_min
        t1 = time()
        elapsed_time = t1 - t0
        print ("%f s\t%f s/entry\tMINIMUM()\t%d times"
               % (elapsed_time, elapsed_time / 1000, 1000))

        # Check that MAXIMUM() operation works:
        t0 = time()
        for i in range(1000):
            assert list.maximum().key == data_max
        t1 = time()
        elapsed_time = t1 - t0
        print ("%f s\t%f s/entry\tMAXIMUM()\t%d times"
               % (elapsed_time, elapsed_time / 1000, 1000))

        # Check that SUCCESSOR() operation works:
        t0 = time()
        for i in range(1, test_size - 2):
            assert list.successor(list.get(i)).key == data[test_size - 2 - i]
        t1 = time()
        elapsed_time = t1 - t0
        print ("%f s\t%f s/entry\tSUCCESSOR()\t%d entries"
               % (elapsed_time, elapsed_time / (test_size - 2), test_size - 2))

        # Check that PREDECESSOR() operation works:
        t0 = time()
        for i in range(1, test_size - 2):
            assert list.predecessor(list.get(i)).key == data[test_size - i]
        t1 = time()
        elapsed_time = t1 - t0
        print ("%f s\t%f s/entry\tPREDECESSOR()\t%d entries"
               % (elapsed_time, elapsed_time / (test_size - 2), test_size - 2))

        # Check that DELETE() operation works:
        t0 = time()
        for i in data[:test_size / 2]:
            list.delete(list.search(i))
        t1 = time()
        elapsed_time = t1 - t0
        print ("%f s\t%f s/entry\tDELETE()\t%d entries"
               % (elapsed_time, elapsed_time / (test_size / 2), test_size / 2))

        # Check that the remaining nodes still exist:
        for i in data[test_size / 2:]:
            assert list.search(i).key == i

        print
