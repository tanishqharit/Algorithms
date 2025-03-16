# We can unpack a list or a tuple if we know their length, we can assignment
# each element into a seprate variable.

from typing import List, Tuple

def sum_3_integers(triplet: List[int]) -> int:
    a, b, c = triplet
    sum = a + b + c
    return sum

def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    width, height, depth = box_dimensions
    volume = width * height * depth
    return volume

print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))

'''
Output:
6
12
6
6
189
'''