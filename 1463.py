N = int(input())

dp = [0] * 10000000

# i는 2부터 시작 2부터 N까지 만들어지는 경우 확인
# dp 1은 0
# dp 2는 dp1 + 1에 
# dp 3은 
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1) 
    
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])
