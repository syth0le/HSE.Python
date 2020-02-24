naturNum = int(input())
massive = list(map(int, input().split()))  # массив с данными
workNum = int(input())
maxDeepToNum = -1000000
minHeightToNum = 1000000
for i in range(naturNum):
    if massive[i] > workNum:
        if minHeightToNum > massive[i]:
            minHeightToNum = massive[i]
    elif massive[i] < workNum:
        if maxDeepToNum < massive[i]:
            maxDeepToNum = massive[i]
    elif massive[i] == workNum:
        maxDeepToNum = massive[i]
        minHeightToNum = maxDeepToNum
if maxDeepToNum == minHeightToNum:
    print(minHeightToNum)
elif maxDeepToNum == 0:
    print(minHeightToNum)
elif minHeightToNum == 1000000:
    print(maxDeepToNum)
elif maxDeepToNum < workNum:
    a = maxDeepToNum - workNum
    b = -a
    if b > minHeightToNum - workNum:
        print(minHeightToNum)
    else:
        print(maxDeepToNum)
else:
    print(maxDeepToNum)
