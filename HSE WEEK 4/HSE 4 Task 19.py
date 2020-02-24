import math


def sumLen():
    n = int(input())
    if n == 0:
        return 0
    return n + sumLen()


print(sumLen())
