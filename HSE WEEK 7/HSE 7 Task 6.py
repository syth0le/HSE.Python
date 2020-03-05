inFile = open('7_week_input.txt', 'r', encoding="UTF8")
text = inFile.readlines()
textSet = set()
for line in text:
    textSet.add(line.split())
sSet = textSet.sorted()
print(len(sSet))
