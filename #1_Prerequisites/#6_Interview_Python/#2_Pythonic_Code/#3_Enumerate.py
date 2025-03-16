# Suppose we wanted to loop over an array 
# and we needed to access both the index and the element at that index.
# We can do this using enumerate() function.
from typing import List

def get_index_of_seven(nums: List[int]) -> int:
    
    for index, element in enumerate(nums):
        if element == 7:
            return index
    return -1

def get_dist_between_sevens(nums: List[int]) -> int:
    
    first_seven_index = -1
    for index, element in enumerate(nums):
        if element == 7:
            if first_seven_index == -1:
                first_seven_index = index
            else:
                return index - first_seven_index

print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))

'''
Output:
6
-1
2
4
1
5
'''