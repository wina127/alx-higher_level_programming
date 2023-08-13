#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for alex in matrix:
        for tom in alex:
            print("{:d}".format(tom), end=" " if tom != alex[-1] else "")
            print()
