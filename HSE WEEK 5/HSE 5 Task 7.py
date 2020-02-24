number = int(input())
i = 1
previous = 0
for i in range(0, number):
    for j in range(1, i + 2):
        print(j, end='')
    print()
