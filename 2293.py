N, K = map(int, input().split())

O = [int(input()) for _ in range(N)]
dp = [0] * (K+1)
dp[0] = 1


for coin in O:
    for j in range(coin, K+1):
        dp[j] += dp[j-coin]
        
print(dp[K])