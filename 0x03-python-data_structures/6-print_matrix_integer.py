#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''a function that  that prints a matrix of integers'''
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
