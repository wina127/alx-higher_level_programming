#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    j = 1
    for i in range(len(argv)-1):
        sum = sum + int(argv[j])
        j += 1
print("{}".format(sum))
