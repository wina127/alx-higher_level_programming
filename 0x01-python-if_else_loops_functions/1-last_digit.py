#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if number < 0:
    last_digit *= -1

#approprite message

    if last_digit > 5:
        message = "is greater than 5"
    elif last_digit == 0:
        message = "is 0"
    else:
        message = "is less than 6 and not 0"
    print(f"last digit of {number:d} is {last_digit:d} and is", {
        message})
