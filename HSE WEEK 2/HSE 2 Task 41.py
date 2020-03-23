a = int(input())
f1 = 0
f2 = 1
k = 0
f = 0
if a == 0:
    print(0)
elif a == 1:
    print(1)
elif a >= 2:
    while f <= a:
        f = f1 + f2
        f1 = f2
        f2 = f
        k += 1
        if f1 == a:
            h = k
        else:
            h = -1
    print(h)
