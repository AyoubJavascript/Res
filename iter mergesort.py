import math



################################################
def merge(L1,L2) :
    i = 0
    j = 0
    merged = []
    while i < len(L1) and j < len(L2) :
        if L1[i] <= L2[j] :
            merged.append(L1[i])
            i += 1
            if i >= len(L1) : break
        if L1[i] > L2[j] :
            merged.append(L2[j])
            j += 1
            if j >= len(L2): break
    if i == len(L1) :
        merged.extend(L2[j:])
    if j == len(L2) :
        merged.extend(L1[i:])
    return merged
##################################
L = [2,3,7,0,-1]
def merge_sort(L):
    list = [ [x] for x in L]
    while len(list) > 1 :
        for i in range(0, len(list)):
            if i >= len(list) - 1: break
            list[i] = merge(list[i], list[i + 1])
            list.pop(i + 1)
    print(list[0])

merge_sort(L)
