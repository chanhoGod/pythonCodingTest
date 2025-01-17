import sys

read = sys.stdin.readline


N, M = map(int, input().split())

O = [0] + [int(i) for i in input().split()]

D = [0] * (N + 1)

for i in range(1, N + 1):
    D[i] = O[i] + D[i-1]

D = D[1:]
C = [0] * M
total_cnt = 0

for i in range(N):
    a = D[i] % M
    
    if a == 0:
        C[a] = C[a] + 1
        total_cnt += 1
    else:
        C[a] = C[a] + 1

for i in range(M):
    num = (C[i] * (C[i] - 1)) // 2
    total_cnt += num
    
print(total_cnt)