#!/usr/bin/python3
def fizzbuzz():
    """print the numbers from 1 to 100 separated by a space.

    for multiples of three, prit Fizz instead of the number.
    for multiples of five, prin Buzz instead of the number.
    for multiples of three and five, print FizzBuzz instead of the number.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 ==0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
