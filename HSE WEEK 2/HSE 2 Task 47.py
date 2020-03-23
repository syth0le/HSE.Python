n = int(input())
minNum = 100
k = 0
h = 1
pred1 = 0
pred2 = 0
u = 0
while n != 0:
    if h >= 3:
        if pred2 < pred1 > n:
            if u >= 1:
                if k <= minNum:
                        minNum = k
            k = 1
            u = 1
        elif ((u >= 1) and ((pred2 <= pred1 <= n) or
                            (pred2 >= pred1 >= n) or
                            (pred2 >= pred1 <= n))):
            if h > 3:
                k += 1
    pred2 = pred1
    pred1 = n
    n = int(input())
    h += 1
if minNum == 100:
    print(0)
else:
    print(minNum)
