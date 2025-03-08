import sys

N, M = map(int, input().split())

O = [[sys.maxsize for i in range(N+1)] for j in range(N+1)]

for i in range(N+1):
    for j in range(N+1):
        if i == j:
            O[i][j] = 0

for i in range(M):
    a, b = map(int, input().split())
    O[a][b] = 1
    O[b][a] = 1


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            O[i][j] = min(O[i][j], O[i][k] + O[k][j])

minval = sys.maxsize
result = 0

for i in range(1, N+1):
    sumval = sum(O[i][1:])
    
    if minval > sumval:
        result = i
        minval = sumval

print(result)