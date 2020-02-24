class Man():
    last_name = ''
    rate = 0


def manKey(man):
    return (-man.rate, man.last_name, )


num = int(input())
massivePeople = []
for i in range(num):
    manList = input().split()
    man = Man()
    man.rate = int(manList[1])
    man.last_name = str(manList[0])
    massivePeople.append(man)
massivePeople.sort(key=manKey)
for man in massivePeople:
    print(man.last_name)
## commit

