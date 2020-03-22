x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if 8 >= x1 >= 1 and 8 >= y1 >= 1:
    if 8 >= x2 >= 1 and 8 >= y2 >= 1:
        if (x1 + y1 + x2 + y2) % 2 == 0:
            if y2 > y1:
                print('YES')
            else:
                print('NO')
        elif (x1 + y1 + x2 + y2) % 2 == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
