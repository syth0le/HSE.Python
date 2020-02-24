import math


def power(a, n):
    if n == 0:
        return 1
    else:
        return (a * power(a, n - 1))


a = float(input())
n = float(input())
print("{0:.6}".format(power(a, n)))
