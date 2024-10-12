n = int(input("Enter the value of n:"))
tas = [3,8,9,0,-1,15,27,4,0,1,29]
#############################################""
def switch(x,y):
    tas[x],tas[y] = tas[y],tas[x]
####################################################
def heapsort(p):

    if n*p + 1 >= len(tas) : return

    children_indices = [n * p + i for i in range(1, n + 1) if n * p + i < len(tas)]

    if children_indices:
        min_child = min(children_indices, key=lambda i: tas[i])

    if tas[min_child] < tas[p] :
        switch(p , min_child)

    for i in range(1,n+1):
        heapsort(n*p+i)
######################################################
def heap_check():
    for p in range(len(tas) // n):
        for i in range(1, n + 1):
            if n * p + i < len(tas) and tas[p] > tas[n * p + i]:
                return False
    return True

##########################################################
# Sorting the heap until it becomes valid
while not heap_check():
    heapsort(0)

##########################################################
while not heap_check():
    heapsort(0)
print(tas)








