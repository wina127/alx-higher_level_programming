#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    prints all integers of a list

    args:
    my_list: the list argument whose items will be printed
    """
for i in my_list:
    print("{:d}".format(i))
    #print numbers 1-5
    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)
