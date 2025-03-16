# Python does not have built-in Stack data strcuture,
# but we can use lists.
'''
Stack Operations:
    1. append() : used to push an element onto the stack.
    2. pop() : remove and return the top element from the stack.
    3. -1 : to access top element of the stack without removing it, peeking.
    4. len() : Length of stack.
'''

stack = []
print(f'Original Stack : {stack}')

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(f'Updated Stack : {stack}')

stack.pop()
stack.pop()
print(f'Updated Stack : {stack}')

stack[-1]
print(f'Updated Stack : {stack}')

print(f'Length of Stack : {len(stack)}')

'''
Output:
Original Stack : []
Updated Stack : [1, 2, 3, 4]
Updated Stack : [1, 2]
Updated Stack : [1, 2]
Length of Stack : 2
'''

from typing import List

# takes a list of integers and returns a new list of the integers in reverse order.
def reverse_list(array : List[int]) -> List[int]:
    
    array_reverse = []
    while len(array) > 0:
        array_reverse.append(array.pop())
    return array_reverse

print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))

'''
Output:
[3, 2, 1]
[2, 6, 4, 1, 2, 3]
[2, 6, 4, 1, 2, 3, 7, 9, 1]
'''