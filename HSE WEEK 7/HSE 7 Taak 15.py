emDict = {}
num = int(input())
for i in range(num):
    wordList = list(input().split())
    emDict[wordList[0]] = wordList[1]
    emDict[wordList[1]] = wordList[0]
print(emDict[input()])
