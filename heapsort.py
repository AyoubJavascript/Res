tas = [0,1,2,3,4,5,6,7,8,9,11,20,-1,-8,-6]
mid = len(tas)//2
def reparer(p):
    if 2*p + 2 >= len(tas):
        if tas[2*p + 1] > tas[p]:
            switch(p,2*p + 1)
            return
    if 2*p + 2 <= len(tas) - 1:
        if tas[2 * p + 1] > tas[p] and tas[2 * p + 1] >= tas[2 * p + 2]:
            switch(p, 2 * p + 1)
            return
        if tas[2 * p + 2] > tas[p] and tas[2 * p + 2] >= tas[2 * p + 1]:
            switch(p, 2 * p + 2)
            return

def switch(x,y):
    tas[x],tas[y] = tas[y],tas[x]
for x in range(mid):
    p = 0
    while  2*p+2 <= len(tas) :
        reparer(p)
        p += 1

print(tas)
