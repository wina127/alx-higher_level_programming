#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = abs(number) % 10
if last_number < 6 and last_number != 0:
    print('Last digit of {} is {} less than \
            6 and not 0'.format(number, last_number))
    if last_number > 5:
        print('Last digit of {} is {} and is greater \
                than 5'.format(number, last_number))
        is last_number == 0:
            print('Last digit of {} is {} and is 0'.format(number, last_number))
