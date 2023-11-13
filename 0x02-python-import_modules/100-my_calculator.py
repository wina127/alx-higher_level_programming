#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
if __name__ == "__main__":
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op_symbol = {"+": add, "-": sub, "*": mul, "/": div}
    operator = argv[2]

    if operator not in op_symbol:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    result = op_symbol[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
