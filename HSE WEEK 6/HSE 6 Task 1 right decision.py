list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))


def merge(A: list, B: list):
    len_a = len(A)
    len_b = len(B)

    if len(A) > len(B):
        A, B = B, A
        len_a, len_b = len_b, len_a

    i = 0
    j = 0
    new_list = []

    while i <= len_a:

        if i == len_a:
            new_list = new_list + B[j:len_b]
            return new_list
        elif j == len_b:
            new_list = new_list + A[i:len_a]
            return new_list

        if A[i] < B[j]:
            new_list.append(A[i])
            i += 1
        elif A[i] == B[j]:
            new_list.append(A[i])
            new_list.append(B[j])
            i += 1
            j += 1
        else:
            new_list.append(B[j])
            j += 1


print(*merge(list1, list2))
