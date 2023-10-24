#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    """Print x elememts of a list"""

    retn = 0

    for i in range(x):

        try:

            print("{}".format(my_list[i]), end="")

            retn += 1

        except IndexError:
 
            break

    print("")

    return (retn)


