numList = input().split()
for i in range(0, len(numList), 2):
    numList[i:i+2] = numList[i:i+2][::-1]
readylist = list(map(str, numList))
print(' '.join(readylist))
