def ReduceFraction(n, m):
    maxnm = max(n, m)
    minnm = min(n, m)
    if maxnm == minnm and maxnm * minnm != 0:
        return 1, 1
    else:
        x = maxnm % minnm
        while x > 0:
            maxnm = minnm
            minnm = x
            x = maxnm % minnm

        return n // minnm, m // minnm


a = int(input())
b = int(input())
print(*ReduceFraction(a, b))
