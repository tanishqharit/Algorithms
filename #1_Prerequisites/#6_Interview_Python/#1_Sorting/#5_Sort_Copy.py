# .sorted() function returns a new list with the elements sorted in a specific order.
# The original lists remain unchanged.
# You can also pass a custom function to the 'key' parameter to specify the sorting criteria.

from typing import List

def sort_words(words: List[str]) -> List[str]:
    sorted_words = sorted(words)
    return sorted_words

def sort_numbers(numbers: List[int]) -> List[int]:
    sorted_numbers = sorted(numbers, key = lambda x: abs(x), reverse = True)
    return sorted_numbers

original_words = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]
print(original_words)
print(sort_words(original_words))

original_numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]
print(original_numbers)
print(sort_numbers(original_numbers))

'''
Output:
['cherry', 'apple', 'blueberry', 'banana', 'watermelon', 'zucchini', 'kiwi', 'pear']
['apple', 'banana', 'blueberry', 'cherry', 'kiwi', 'pear', 'watermelon', 'zucchini']
[1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]
[-19, 11, 9, 7, -6, 6, -5, 5, 4, -4, -3, 2, -2, 2, 1]
'''