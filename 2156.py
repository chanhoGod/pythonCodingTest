import sys


read = sys.stdin.readline

N = int(read())
O = [int(read()) for i in range(N)]

DP = [0] * N
DP[0] = O[0]
if N > 1:
    DP[1] = O[0] + O[1]
if N > 2:
    DP[2] = max(O[0] + O[2], O[1] + O[2], DP[1])
if N > 3:
    for i in range(3, N):
        DP[i] = max(O[i] + DP[i-2], O[i] + O[i-1] + DP[i-3], DP[i-1])

print(max(DP))