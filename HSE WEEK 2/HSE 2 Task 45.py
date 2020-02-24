num = int(input())
save = 0
h = 1
while num != 0:
    if num == save:
        save = num
        h += 1
        num = int(input())
    elif num != save:
        save = num
        num = int(input())
print(h)
