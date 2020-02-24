import math
n = int(input())


def MinDivisor(n):
    i = 2
    while n % i != 0:
        if i >= math.sqrt(n):
            return n
        i += 1


def IsPrime(n):
    if n == MinDivisor(n):
        return True
    else:
        return False


if n == 2:
    print('YES')
elif IsPrime(n):
    print('YES')
else:
    print("NO")
