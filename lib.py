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

        print "%fs  %d integers" % (elapsed_time, test_size)
