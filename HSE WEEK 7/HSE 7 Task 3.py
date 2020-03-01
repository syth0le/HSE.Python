f_set = set(list(map(int, input().split())))
s_set = set(list(map(int, input().split())))
result = []
for i in f_set:
    if i in s_set:
        result.append(i)
print(*sorted(result))
