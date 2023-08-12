#!/usr/bin/python3

if _name_ == "_main_":
    ""handle basic arithmetic operations. """
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) -1 != 3:
    print("usage: ./100-my_calculation.py <a>
    <operator> <b>")
    sys.exit(1)

    ops = {"+": add, "_": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
    print("unknown operator. Available operators: +, -, * and /")
