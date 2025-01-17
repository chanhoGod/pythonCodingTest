import sys

read = sys.stdin.readline

N, M = map(int, read().strip().split())


NM_list = [0 * (N+1)]

for i in range(N):
    row = [0] + list(map(int, read().strip().split()))
    NM_list.append(row)

sum_list = [[0 for _ in range(N+1)] for _ in range(N+1)]


for i in range(1, N + 1):
    for j in range(1, N + 1):
        sum_list[i][j] = sum_list[i][j-1] + sum_list[i-1][j] + NM_list[i][j] - sum_list[i-1][j-1]

for i in range(M):
    a, b, c, d = map(int, read().strip().split())
    
    sumnum = sum_list[c][d] - sum_list[c][b-1] - sum_list[a-1][d] + sum_list[a-1][b-1]
    print(sumnum)