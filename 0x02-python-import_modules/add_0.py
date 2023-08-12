#!/usr/bin/python3
a = 1
b = 2

if _name_ == "_main_":
    from add_0 import add

    result = add(a, b)
    print("{} + {} = {}".format(a,b, result))
