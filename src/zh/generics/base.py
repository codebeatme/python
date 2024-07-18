from typing import TypeVar

T = TypeVar('T', int, str)

def sum(a: T, b: T) -> T:
    return a + b

number = sum(1, 2)
string = sum('a', 'b')
number2 = sum(1.1, 2.2)
print(number.is_integer())
print(string.upper())
print(number2)
