listNum = list(map(int, input().split()))


def CountSort(listNum):
    listNum = list(map(int, input().split()))
    len_num = len(listNum)
    numMassive = [] * len_num
    for nums in listNum:
        numMassive[nums] += 1
    for nowMassive in range(len_num):
        print((str(nowMassive) + ' ') * numMassive[nowMassive], end='')


print(CountSort(listNum))
