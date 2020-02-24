num = int(input())
for i in range(10 ** num - 1, 10 ** (num - 1) - 1, -1):
    if i % 2 == 0:
        print(end=" ")
    elif i % 2 == 1:
        print(i, end="")
