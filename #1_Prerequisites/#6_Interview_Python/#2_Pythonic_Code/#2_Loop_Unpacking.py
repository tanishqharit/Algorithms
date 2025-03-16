# We can also use unpacking in loops to iterate over a list of lists.
# This is useful when we know the size of the inner lists and want to unpack them into variables.

from typing import List, Tuple

def best_student(scores: List[Tuple[str, int]]) -> str:
    best_score, best_student_name = 0, ""

    for student, score in scores:
        if score > best_score:
            best_score, best_student_name = score, student
    return best_student_name

print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))

'''
Output:
Alice
Charlie
Bob
David
'''