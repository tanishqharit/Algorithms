# Some functions related to basic list operations.

from typing import List

# append the elements of array_2 to the end of array_1 and return the resulting list.
def append_elements(array_1 : List[int], array_2 = List[int]) -> List[int]:
    
    for element in array_2:
        array_1.append(element)
    return array_1

# remove n elements from the list, if list length lesser than n, return empty list.
def pop_elements(array : List[int], n: int) -> List[int]:
    
    while n > 0 and array:
        array.pop()
        n = n - 1
    return array

# insert element at a specific index, if index out of bounds, return end of the list
def insert_at(array : List[int], index : int, element : int) -> List[int]:
    
    if index < 0 and index >= len(array):
        array.append(element)
    else:
        array.insert(index, element)
    return array

print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_elements([1, 2, 3, 4, 5], 2))
print(pop_elements([1, 2, 3, 4, 5], 6))
print(pop_elements([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))

'''
Output:
[1, 2, 3, 4, 5, 6]
[4, 3, 4, 5, 3]
[1, 2, 3]
[]
[]
[1, 2, 6, 3, 4, 5]
[1, 2, 3, 4, 5]
'''