import sys

read = sys.stdin.readline

N = int(read())
O = []
for i in range(N):
    O.append(int(read()))

O.sort(reverse=True)
result = 0
for i in range(len(O)):
    val = O[i] * (i+1)
    result = max(result, val)
    

print(result)