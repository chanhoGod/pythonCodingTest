N = int(input())

# 45656 인접한 모든 자리의 차이가 1인수를 계단수 라고함
# 숫자 N이 주어질때 길이가 N인 계단수는 몇개가 있나?
# 기본적인 점화식은 dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]로 진행이 됨 이전 자릿수의 마지막 차수의 값을 기준으로 다음 값이 전개되기 때문.

dp = [[0] * 10 for _ in range(N)]

for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, N):
    for j in range(0, 10):
        if j == 0 :
            dp[i][j] = dp[i-1][j+1]
        elif j == 9 : 
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

result = sum(dp[N-1]) % 1000000000

print(result)