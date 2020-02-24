def merge(A, B):
    rez = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            rez.append(A[i])
            i += 1
        else:
            rez.append(B[j])
            j += 1
    rez += A[i:] + B[j:]
    return rez


list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
print(merge(list1, list2))
