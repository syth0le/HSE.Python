num_list = list(map(int, input().split()))
num_set = set()
for elem in num_list:
    if elem in num_set:
        print('YES')
    else:
        print('NO')
        num_set.add(elem)
