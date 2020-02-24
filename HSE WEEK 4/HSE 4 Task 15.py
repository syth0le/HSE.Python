import math


def NOD(a, b):
    while a % b:
        a, b = b, a % b
    return b


a = int(input())
b = int(input())
print(NOD(a, b))
