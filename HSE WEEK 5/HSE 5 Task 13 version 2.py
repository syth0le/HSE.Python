numList = list(map(int, input().split()))                #неработающая хрень
long = len(''.join(map(str, numList)))
for i in range(0, long):
    if numList[i-1] % 2 == 0:
        print(numList[i], end='')
print([i for i in numList if numList[i] % 2 == 0])
