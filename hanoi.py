L = [8, 7, 6, 5, 4, 3, 2, 1, 0]
dep, res, arr = L.copy(), [], []

def hanoi(n, dep, res, arr):
    if n == 0:
        return
    hanoi(n - 1, dep, arr, res)
    x = dep.pop()
    arr.append(x)
    hanoi(n - 1, res, dep, arr)

hanoi(len(L), dep, res, arr)
print(arr)
