# We can also use 'lambda' function to define a function in a single line 
# and pass it directly to the .sort() method.
# A lambda function must be single expression and it cannot contain multiple statements.

from typing import List

def sort_words(words: List[str]) -> List[str]:
    words.sort(key = lambda word: len(word), reverse = True)
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key = lambda numbers: abs(numbers))
    return numbers

print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))
print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))

'''
Output:
['watermelon', 'blueberry', 'zucchini', 'cherry', 'banana', 'apple', 'kiwi', 'pear']
[1, 2, -2, 2, -3, 4, -4, -5, 5, -6, 6, 7, 9, 11, -19]
'''