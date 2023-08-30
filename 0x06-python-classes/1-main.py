#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(1-square))
print(1-square.__dict__)

try:
    print(1-square.size)
except Exception as e:
    print(e)

try:
    print(1-square.__size)
except Exception as e:
    print(e)
