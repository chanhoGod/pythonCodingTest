import sys


read = sys.stdin.readline

N = int(read())

O = list(map(int, read().split()))

DP = [0] * N
DP[0] = O[0]

for i in range(1, N):
    DP[i] = max(DP[i-1] + O[i], O[i])

print(max(DP))