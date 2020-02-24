import math


def multiplication(a, n):
    if a % 2 == 0:
        digit = ((a ** 2) ** (n / 2))
        return digit
    elif a % 2 == 1:
        digit2 = (a * a ** (n - 1))
        return digit2
    else:
        return a ** n


a = float(input())
n = float(input())
print('{0:.6}'.format(multiplication(a, n)))
