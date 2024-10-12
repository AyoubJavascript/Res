
n = int(input())
x= 0

for i in range(n):
    op = input().strip()
    if op == "--X" or op =="X--":
        x -= 1
    elif op == "X++" or op == "++X" :
        x += 1
print(x)