def quicksort(L):
    if len(L) <= 1: return L
    pivot = L[0]
    left , mid,right = [] , [] , []
    for i in L:
        if i < pivot:
            left.append(i)
        elif i > pivot :
            right.append(i)
        elif i == pivot :
            mid.append(i)
    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([9,7,10,76,12,1,25]))
