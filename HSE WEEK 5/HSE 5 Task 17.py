numList = input().split()
k = int(numList[2])
long = len(numList)
for i in range(0, long):
    if int(numList[i]) >= k:
        print(numList[i], end=' ')
    k = int(numList[i])
