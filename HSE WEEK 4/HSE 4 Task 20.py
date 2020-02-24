import math


def reverse():
    n = int(input())
    if n != 0:
        reverse()
        print(n)
    elif n == 0:
        print(0)


reverse()
