a = int(input())
b = int(input())
c = int(input())
if a % 2 == 0 and (b + 1) % 2 == 0:
    print('YES')
elif a % 2 == 0 and (c + 1) % 2 == 0:
    print('YES')
elif b % 2 == 0 and (c + 1) % 2 == 0:
    print('YES')
elif b % 2 == 0 and (a + 1) % 2 == 0:
    print('YES')
elif c % 2 == 0 and (a + 1) % 2 == 0:
    print('YES')
elif c % 2 == 0 and (b + 1) % 2 == 0:
    print('YES')
else:
    print('NO')
