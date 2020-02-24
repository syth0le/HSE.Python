n = int(input())
if n == 11 or n == 12 or n == 13 or n == 14 or n == 15:
    print(n, 'korov')
elif n == 16 or n == 17 or n == 18 or n == 19:
    print(n, 'korov')
elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
    print(n, 'korovy')
elif n % 10 == 1:
    print(n, 'korova')
else:
    print(n, 'korov')
