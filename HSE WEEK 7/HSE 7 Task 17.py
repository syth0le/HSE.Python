inFile = open('7_week_input.txt', 'r', encoding="UTF8")
lines = inFile.read()
text = lines.split()
emDict = {}
rezDict = {}
numMassive = []
for word in text:
    if word in emDict:
        emDict[word] -= 1
    else:
        emDict[word] = 0
for word in emDict:
    numMassive.append((emDict[word], word))
for massive in numMassive:
    rezDict[massive[1]] = massive
rez = min(rezDict.values())
print(rez[1])
