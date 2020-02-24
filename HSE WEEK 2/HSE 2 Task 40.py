n = int(input())
save = 1
save2 = 1
while n > 0:
    if n == 1:
        n -= 1
        print(0)
        break
    elif n <= 3:
        save3 = save + save2
        save = save
        save2 = save2
        print(save2)
        break
    else:
        save = save2
        save3 = save + save2
        save2 = save3
        n -= 1
        print(save)
        continue
херня ссаная
