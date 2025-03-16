# More List Operations
'''
    1. index() : return first occurance index of a specified element in a list.
        If element no present - ValueError
    2. remove() : Removes the first occurrence of a specified element from the list.
    3. extend() : Adds the elements of another list to the end of the list.
'''

list = [1, 3, 2, 3]
print(list.index(3))
list.remove(3)
list.extend([4, 5])
print(list)

'''
Output
1
[1, 2, 3, 4, 5]
'''

from typing import List

# append the elements of array2 to the end of array1 and return the resulting list.
def append_elements(array1 : List[int], array2 : List[int]) -> List[int]:
    
    array1.extend(array2)
    return array1

# remove all elements of arr2 from arr1 and return the resulting list.
# If any of the elements in arr2 are not in arr1, then skip them.
def remove_elements(array1 : List[int], array2 : List[int]) -> List[int]:
    
    for element in array2:
        if element in array1:
            array1.remove(element)
    return array1

print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))

'''
Output:
[1, 2, 3, 4, 5, 6]
[4, 3, 4, 5, 3]
[1, 3, 5]
[1]
[1, 3, 4, 5]
'''