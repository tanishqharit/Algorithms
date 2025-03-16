# Some languages have both fixed-size arrays and resizable arrays.
# Python, we only have resizable arrays, which are referred to as Lists.
# This means that we can add or remove elements from a list at any time.
'''
List Common Operations/Methods:
    1. append() : adds an element to end of the list.
    2. pop() : removes and returns last element of the list.
        a) If list already empty, IndexError.
        b) We can also pass an integer to pop() to remove an element at specefic index.
        c) If we pop(index) an index that is out of bounds, IndexError.
    3. insert() : Inserts an element at a specified index in the list.
        a) f the index is out of bounds, IndexError.
'''

list = [1,2,3,4,5]
print(f'Original List: {list}')

list.append(10)
list.append(11)
list.append(12)
print(f'Updated List : {list}')

list.pop()
list.pop(2)
print(f'Updated List : {list}')

list.insert(1, 100)
print(f'Updated List : {list}')

'''
Output:
Original List: [1, 2, 3, 4, 5]
Updated List : [1, 2, 3, 4, 5, 10, 11, 12]
Updated List : [1, 2, 4, 5, 10, 11]
Updated List : [1, 100, 2, 4, 5, 10, 11]
'''