#!/usr/bin/env python
#
## Arrays and Strings:
#
# Solutions for the code questions posed in Cracking the Code
# Interview, Chapter 1, page 73.
#

# Exercise 1.1:
#
#     Implement an algorithm to determine if a string has all unique
#     characters. What if you cannot use additional data structures?
#
# This is a variation on the "count the number of times each character
# appears in a string", except that we only need two store two
# possible values: character present, or character not present. On the
# first occurrence of a character recurring, we can return false.
#
# The solution we've implemented operates in O(n) time, with a best
# case time of O(1) (when string length > 256). It operates with O(1)
# space complexity.
#
def characters_are_unique(string):

    # This is a crafty optimisation: since we know the character space
    # is 256 (the number of characters in the ASCII character set),
    # then by definition any string that is longer than this *must*
    # include duplicate characters:
    if len(string) > 256:
        return False

    # We need 256 bytes in order to store our set of character
    # occurrences. If we were interested in bit twiddling, we could
    # reduce the memory footprint by 7/8 by using an array of bytes of
    # using individual bits to represent each character:
    characters = [False] * 256

    for c in string:
        val = ord(c)

        if characters[val] == True:
            return False
        else:
            characters[val] = True

    return True

# Exercise 1.3:
#
#     Given two strings, write a method to decide if one is a
#     permutation of the other.
#
# A permutation of a string must contain the exact same characters,
# but may contain them in any order. To check whether one string is a
# permutation of another, we can sort the characters within both
# strings in the same way, and check whether these sorted character
# arrays match. The efficiency of this algorithm will depend on the
# efficiency of the sorting algorithm used, as will the memory
# footprint (depends on whether the strings are sorted in place).
#
# An alternative implementation would be to check if the two strings
# have identical character counts, but this requires a priori
# knowledge of the size of the character sets.
def is_permutation(a, b):

    if len(a) != len(b):
        return False

    # Depending on how efficient this comparison is, we may want to
    # skip it.
    if a == b:
        return True

    return sorted(list(a)) == sorted(list(b))

if __name__ == "__main__":

    # Exercise 1.1
    assert characters_are_unique("abcdefg") == True
    assert characters_are_unique("abcdefga") == False

    # Exercise 1.3
    assert is_permutation("abc", "abc") == True
    assert is_permutation("abc", "abcd") == False
    assert is_permutation("abc", "cab") == True
