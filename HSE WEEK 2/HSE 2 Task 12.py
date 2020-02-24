vertical1 = int(input())
horizon1 = int(input())
vertical2 = int(input())
horizon2 = int(input())
if vertical1 + 1 == vertical2 and horizon1 + 1 == horizon2:
    print('YES')
elif vertical1 - 1 == vertical2 and horizon1 + 1 == horizon2:
    print('YES')
else:
    print('NO')
