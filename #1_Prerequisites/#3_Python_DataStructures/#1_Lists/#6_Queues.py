# Python provides deque class from the collections module,
# that can be used to implement queue.
'''
Queue Operations:
    1. append() : to enqueue an element to the right side of stack.
    2. popleft() : to remove and return leftmost element from the stack. 
    3. [0] and [-1] : to access leftmost and rightmost elements of the queue respectively.
        Assuming queue is not empty.
    4. len() : can be used to check if the queue is empty.
'''

from collections import deque
from typing import List, Deque

# Initialisation - empty queue 
queue = deque()
print(f'Original Queue : {queue}')

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(f'Updated Queue : {queue}')

queue.popleft()
print(f'Updated Queue : {queue}')

print(f'Leftmost Element = {queue[0]}')
print(f'Rightmost Element = {queue[-1]}')

while len(queue) > 0:
    print(queue.popleft())

'''
Output:
Original Queue : deque([])
Updated Queue : deque([1, 2, 3, 4])
Updated Queue : deque([2, 3, 4])
Leftmost Element = 2
Rightmost Element = 4
2
3
4
'''

# takes a list of integers arr and an integer k 
# convert the list into a deque, then rotate the values in the list to the left by k steps 
# and return the resulting deque.
def rotate_list(array : List[int], k : int) -> Deque[int]:
    
    queue = deque(array)
    
    for i in range(k):
        queue.append(queue.popleft())
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
deque([2, 3, 4, 5, 1])
deque([3, 4, 5, 1, 2])
deque([4, 5, 1, 2, 3])
deque([5, 1, 2, 3, 4])
deque([1, 2, 3, 4, 5])
'''