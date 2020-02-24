import math
a = int(input())
b = int(input())
c = int(input())
if b + c > a and a ** 2 == b ** 2 + c ** 2:
    print('rectangular')
    if a + c > b and b ** 2 == a ** 2 + c ** 2:
            print('rectangular')
            if a + b > c and c ** 2 == a ** 2 + b ** 2:
                print('rectangular')
    if b + c > a and a ** 2 < b ** 2 + c ** 2:
        print('acute')
        if a + c > b and b ** 2 < a ** 2 + c ** 2:
            print('acute')
            if a + b > c and c ** 2 < a ** 2 + b ** 2:
                print('acute')
    if b + c > a and a ** 2 > b ** 2 + c ** 2:
        print('obtuse')
        if a + c > b and b ** 2 > a ** 2 + c ** 2:
            print('obtuse')
            if a + c > b and c ** 2 > a ** 2 + b ** 2:
                print('obtuse')
                    else:
                        print('impossible')
