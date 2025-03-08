import sys

read = sys.stdin.readline

N = int(read().strip())

O = [[0 for i in range(N+1)] for j in range(N+1)]

for i in range(1, N+1):
    A = list(map(int, read().split()))
    
    for j in range(1, N+1):
        O[i][j] = A[j-1]

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if O[i][k] == 1 and O[k][j] == 1:
                O[i][j] = 1

for i in range(1, N+1):
    print(*O[i][1:])