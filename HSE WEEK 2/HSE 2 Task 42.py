a = int(input())
b = int(input())
while a > b:
    if a % 2 == 0:
        if a // 2 >= b:
            a = a // 2
            print(':2')
        else:
            a -= 1
            print('-1')
    elif a % 2 != 0:
        a -= 1
        print('-1')
