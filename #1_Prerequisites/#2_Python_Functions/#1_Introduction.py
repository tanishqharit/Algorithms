# User Defined Functions : To increase code reusibility and readability.

def calc_function(x: float, y: float) -> float:    # Arguments and Return datatype 
    '''Simple Calculator Function'''               # Docstring 
    add = x + y 
    sub = x - y 
    mult = x * y 
    div = x / y 
    result = f'Addition = {add}, Subtraction = {sub}, Muliplication = {mult}, Division = {div}'
    return result

def area(radius, pi = 3.14):     # Default argument must have last position 
    '''Applying pi formulas'''
    print(f'Circle_Area = {pi * radius * radius}') 
    print(f'Circle_Circumference = {2 * pi * radius}')
    print(f'Sphere_Area = {4 * pi * radius * radius}')
    print(f'Sphere_Volume = {(4/3) * pi * radius * radius * radius}')

if __name__ == '__main__':       # Main Function 
    print(calc_function(10, 5))
    area(5)