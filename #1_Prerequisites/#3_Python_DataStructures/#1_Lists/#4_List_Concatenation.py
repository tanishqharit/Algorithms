# Instead of using the extend() method, there's an easier way to concatenate 2 lists.
# We can use the + operator.
# Only difference is between 2 methods are, that + operator create a new list.

list1 = [1,2,3]
list2 = [4,5,6]
result = list1 + list2
print(result)

'''
Output:
[1, 2, 3, 4, 5, 6]
'''

from typing import List

# takes two lists of integers and returns a new list that contains 
# all the elements of the first list followed by all the elements of the second list.
def combine_elements(array1 : List[int], array2 : List[int]) -> List[int]:
    result = array1 + array2
    return result

arr1 = [1, 3, 5]
arr2 = [4, 6, 8]
print(combine_elements(arr1, arr2))
print(arr1)
print(arr2)

'''
Output:
[1, 3, 5, 4, 6, 8]
[1, 3, 5]
[4, 6, 8]
'''