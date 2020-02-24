def merge(a: list, b: list):
    full_list = []
    full_list.extend(a)
    full_list.extend(b)
    mid_of_list = int(len(full_list) / 2)
    one = []
    two = []
    one.extend(full_list[:mid_of_list])
    two.extend(full_list[mid_of_list:])
    i = 0
    j = 0
    new_list = []
    while i <= len(one):
        if one[i] < two[j]:
            new_list.append(one[i])
            i += 1
        elif one[i] == two[j]:
            new_list.append(one[i])
            new_list.append(two[j])
            i += 1
            j += 1
        else:
            new_list.append(two[j])
            j += 1
++++++ hernya ppz
    return new_list


first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))
print(merge(first_list,second_list))