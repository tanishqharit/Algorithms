# Python provides an easy way to iterate over multiple lists at the same time using the zip() function.
# The zip() function takes multiple lists as arguments and returns an iterator of tuples.
# Each tuple contains an element from each list.
# But lists must be of same length.

from typing import List, Dict

def group_names_and_scores(names: List[str], scores: List[int]) -> Dict[str, int]:
    
    group = {}
    for name, score in zip(names, scores):
        group[name] = score
    return group

print(group_names_and_scores(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(group_names_and_scores(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(group_names_and_scores(["Doug", "Bob", "Tommy"], [80, 90, 100]))

'''
Output:
{'Alice': 90, 'Bob': 80, 'Charlie': 70}
{'Jane': 25, 'Carol': 100, 'Charlie': 60}
{'Doug': 80, 'Bob': 90, 'Tommy': 100}
'''