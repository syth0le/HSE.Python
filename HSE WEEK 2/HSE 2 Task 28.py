n = int(input())
i = 1
if i == n:
    print('YES')
while i < n:
    i = i * 2
    if i == n:
        print('YES')
if i != n:
    print('NO')
