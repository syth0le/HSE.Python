numList = list(map(str, input().split()))
readyList = ''
i = -1
for i in range(-1, len(numList)-1):
    readyList += numList[i] + ' '
print(readyList)
