L = [213,132,111,222,333,112,211,312,311,322,323,123,9]

def fix(L):
    lenght = len(str(max(L)))
    for i in range(len(L)) :
        L[i] = str(L[i])
        while len(L[i]) < lenght:
            L[i] = "0" + L[i]

def radix(L,i = 1):
    if i > len(str(L[0])):
        print(L)
        return
    if i == 1 : fix(L)
    bucket = []
    for x in range(10):
        bucket += [n for n in L if str(n)[len(str(n))-i] == str(x)]

    radix(bucket,i+1)
radix(L)