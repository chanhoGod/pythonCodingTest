N, K = map(int, input().split())

O = [int(input()) for i in range(N)]

DP = [0] * (K+1)

DP[0] = 1

for coin in O:
    for j in range(coin, K+1):
        DP[j] += DP[j-coin]

print(DP[K])