import sys


read = sys.stdin.readline

N, M = map(int, read().split())

WV = [list(map(int, read().split())) for _ in range(N)]

DP = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    W, V = WV[i-1]
    
    for j in range(1, M+1):
        if W > j:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-W] + V)

print(DP[N][M])