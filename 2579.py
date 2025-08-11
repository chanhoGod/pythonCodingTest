N = int(input())

O = [0] + [int(input()) for _ in range(N)]

dp = [0] * (301)

if N == 1:
    print(O[1])
elif N == 2:
    print(O[1] + O[2])
else:
    dp[1] = O[1]
    dp[2] = O[1] + O[2]

    for i in range(3, N+1):
        dp[i] = max(dp[i-2] + O[i], dp[i-3] + O[i-1] + O[i])

    print(dp[N])