# We can also specify a custom sort order using key parameter in .sort() method.
# key parameter does not accepts a value 
# instead it accepts a function that returns a value to be used for sorting.

from typing import List

def word_length(word: str) -> int:
    return len(word)

def sort_words(words: List[str]) -> List[str]:
    words.sort(key = word_length, reverse = True)
    return words

def absolute_number(number: int) -> int:
    return abs(number)

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key = absolute_number, reverse = True)
    return numbers

print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))
print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))

'''
Output:
['watermelon', 'blueberry', 'zucchini', 'cherry', 'banana', 'apple', 'kiwi', 'pear']
[-19, 11, 9, 7, -6, 6, -5, 5, 4, -4, -3, 2, -2, 2, 1]
'''