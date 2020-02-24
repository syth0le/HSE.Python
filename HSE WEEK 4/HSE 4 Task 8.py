import math


def xor(x1, x2):
    if x1 == 1 and x2 == 0:
        return True
    elif x1 == 0 and x2 == 1:
        return True
    else:
        return False


x1 = float(input())
x2 = float(input())
if xor(x1, x2) is True:
    print(1)
elif xor(x1, x2) is False:
    print(0)
