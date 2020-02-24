def CountSort(list):
    sortedList = [0] * 101
    for i in list:
        sortedList[i] += 1
    for i in range(101):
        print((str(i) + ' ') * sortedList[i], end='')


list = [int(i) for i in input().split()]
CountSort(list)
