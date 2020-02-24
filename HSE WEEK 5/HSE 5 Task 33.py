numList = list(map(int, input().split()))
deep = numList.index(min(numList))
high = numList.index(max(numList))
numList[deep], numList[high] = numList[high], numList[deep]
print(*numList)
