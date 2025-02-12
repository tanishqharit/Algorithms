# We know Default arguments.

# Keywords arguments
def student(firstname, lastname):
    '''
    Caller has to specify the argument names with the values. 
    So that caller does not need to remember the order of parameters.
    '''
    print(firstname, lastname)

# Positional arguments 
def introductions(name, age):
    '''
    Position of arguments must be maintained when calling the function. 
    '''
    return (f'My name is {name} and I am {age} years old.')

# Arbitrary Keywords arguments - Multiple arguments 
def students(*args):
    for i in args: 
        print(i, end = ' ')
    print()

def information(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value},', end = ' ')

# Main Function 
if __name__ == '__main__':
    student(firstname = 'Tanishq', lastname = 'Harit')
    print(f'Case 1 : {introductions('Tanishq', 24)}')
    print(f'Case 2 : {introductions(24, 'Tanishq')}')
    students('Harry', 'Ron', 'Hagrid', 'Snape')
    information(Name = 'Tanishq', University = 'Stevens Tech', Major = 'Computer Science')

# Output
'''
Tanishq Harit
Case 1 : My name is Tanishq and I am 24 years old.
Case 2 : My name is 24 and I am Tanishq years old.
Harry Ron Hagrid Snape 
Name: Tanishq, University: Stevens Tech, Major: Computer Science,
'''