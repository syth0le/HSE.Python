inFile = open('7_week_input.txt', 'r', encoding="UTF8")
a = []
for i in inFile.read().split('\n'):
    a += i.split()
print(len(set(a)))
