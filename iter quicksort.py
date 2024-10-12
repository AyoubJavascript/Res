def cut(arr : list):
    pivot =  arr[0]
    left,mid,right = [i for i in arr if i < pivot],[i for i in arr if i == pivot ],[ i for i in arr if i > pivot]
    return left , mid , right


L = [9,2,45,98,23,15,65,6,4,123,654,789,32,999,4.5,0,1]
A = [ [L]]
continuer = 1

while continuer == 1 :
    A.append([])
    for liste in A[0]:
        triplet = cut(liste)
        for mini in triplet :
            if mini != [] : A[1].append(mini)
    A.pop(0)

    for h in A[0]:
        if len(h) != 1 : break
        if len(A[0][-1]) == 1 : continuer = 0

result = [i[0] for i in A[0] ]
print(result)
triol=cut(L)
print(triol)