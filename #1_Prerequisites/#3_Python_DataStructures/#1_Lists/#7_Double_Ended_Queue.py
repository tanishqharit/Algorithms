# The deque provided in python is actually Double Ended Queue. 
# It allows you us push and pop from both the sides of queue effeciently.
'''
Deque Operations:
    1. appendleft() : to enqueue an element at the left side of the queue.
    2. pop() : to return and remove the rightmost element from the queue.
'''

from typing import List, Deque
from collections import deque

# takes a list of integers arr and an integer k 
# convert the list into a deque, then rotate the values in the list to the left by k steps 
# and return the resulting deque.
def rotate_list(array : List[int], k : int) -> Deque[int]:
    queue = deque(array)
    for i in range(k):
        queue.appendleft(queue.pop())
    return queue

print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))

'''
Output:
deque([1, 2, 3, 4, 5])
deque([5, 1, 2, 3, 4])
deque([4, 5, 1, 2, 3])
deque([3, 4, 5, 1, 2])
deque([2, 3, 4, 5, 1])
deque([1, 2, 3, 4, 5])
'''