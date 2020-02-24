num = int(input())
save = 0
while num != 0:
    if num >= save:
        save = num
    num = int(input())
print(save)
