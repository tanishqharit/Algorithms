# In python we have .sort() method, to sort elements in a list or an array.
# By default, it sorts in ascending order in-place.
# The return value of .sort() is None.
# This also works for list of string. (Lexicographic order by default)
# Python uses Timsort Algorithm - hybrid of merge sort and insertion sort.

from typing import List

def sort_words(words : List[str]) -> List[str]:
    words.sort()
    return words

def sort_numbers(numbers : List[int]) -> List[int]:
    numbers.sort()
    return numbers

def sort_decimals(decimals : List[float]) -> List[float]:
    decimals.sort()
    return decimals

print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))
print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))
print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))

'''
Output:
'apple', 'banana', 'blueberry', 'cherry', 'kiwi', 'pear', 'watermelon', 'zucchini']
[1, 2, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 9, 11, 19]
[2.82, 3.14, 6.433, 7.9, 21.554, 21.555]
'''