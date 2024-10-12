
tas = [3,8,9,0,-1,15,27,4,0,1,29]
mid = len(tas)//2

def switch(x,y):
    tas[x],tas[y] = tas[y],tas[x]

def heapsort(p):
    if 2*p + 1 >= len(tas) : return
    min_child = 2*p + 1

    if 2*p + 2 <= len(tas) - 1 and tas[2*p + 2] < tas[2*p + 1] : min_child = 2*p + 2

    if tas[min_child] < tas[p] :
        switch(p , min_child)

    heapsort(2*p + 1)
    heapsort(2*p + 2)

def heap_check(tas):
    success = True
    for p in range(mid):
        if tas[p] > tas[2*p + 1] or tas[p] > tas[2*p + 2] : success = False
    return success

while not heap_check(tas) : heapsort(0)

print(tas)

