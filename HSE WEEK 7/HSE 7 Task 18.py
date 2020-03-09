inFile = open('7_week_input.txt', 'r', encoding="UTF8")
lines = inFile.read()
text = lines.split()
emDict = {}
rezDict = {}
numMassive = []
rez = list()
for word in text:
    if word in emDict:
        emDict[word] -= 1
    else:
        emDict[word] = 0
for word in emDict:
    numMassive.append((emDict[word], word))
for massive in numMassive:
    rezDict[massive[1]] = massive
for word in rezDict:
    rez.append(word)
numMassive.sort()
for result in numMassive:
    print(result[1])
