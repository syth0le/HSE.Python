h = int(input())
i = 0
n = 0
while n <= h:
    n = 2 ** i
    if h == n:
        print('YES')
        break
    elif n > h:
        print('NO')
        break
    else:
        i = i + 1
