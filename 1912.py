import sys

read = sys.stdin.readline

N = int(read())
T = [0] + list(map(int, read().split()))
dp = [0] * (N + 1)

for i in range(1, N+1):
    
    dp[i] = max(dp[i-1] + T[i], T[i])

print(max(dp[1:]))