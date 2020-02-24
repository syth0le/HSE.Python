def merge(a, b):
    full_list = []
    full_list.extend(a)
    full_list.extend(b)
    f_len = len(a)пшпмшнжмжшм
    s_len = len(b)
    new_list = []
    print(full_list)
    if len(full_list) % 2 == 0:
        mid_list = int(len(full_list) / 2)
        print(mid_list)
        i = 0
        while int(len(full_list)) >= mid_list > i:
            if int(full_list[i]) < int(full_list[mid_list]):
                new_list.append(full_list[i])
                i += 1
            elif int(full_list[i]) == int(full_list[mid_list]):
                new_list.append(full_list[i])
                new_list.append(full_list[mid_list])
                i += 1
                mid_list += 1
            else:
                new_list.append(full_list[mid_list])
                mid_list += 1
    else:
        mid_list = len(full_list[:-1]) / 2
        i = 0
        j = mid_list
        while j <= len(full_list):
            if full_list[i] < full_list[j]:
                new_list.append(full_list[i])
                i += 1
            elif full_list[i] == full_list[j]:
                new_list.append(full_list[i])
                new_list.append(full_list[j])
                i += 1
                j += 1
            else:
                new_list.append(full_list[j])
                j += 1
    return new_list


first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))
print(merge(first_list, second_list))
