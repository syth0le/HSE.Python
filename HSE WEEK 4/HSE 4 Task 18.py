n = int(input())
k = int(input())
херня какая то press F

def C(n, k):
    if n == k:
        return 1
    if k == 1:
        return 1
    else:
        return C(n - 1, k) + C(n - 1, k - 1)

def N(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return C(n - 1, k) + C(n - 1, k - 1)


print(C(n, k))
print(N(n, k))


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
