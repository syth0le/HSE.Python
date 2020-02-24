numList = list(map(int, input().split()))
len(''.join(map(str, numList)))
i = 0
if len(''.join(map(str, numList))) % 2 == 0:
    numList2 = numList[:-1]
    while i <= len(''.join(map(str, numList2))):
        print(numList2[i], end=' ')
        i += 2
else:
    while i <= len(''.join(map(str, numList))):
        print(numList[i], end=' ')
        i += 2
