N = int(input())

DP = [-1] * (N+4)
DP[1] = 1
DP[2] = 0
DP[3] = 1

for i in range(4, N+1):
    if DP[i-1] == 1 and DP[i-3] == 1:
        DP[i] = 0
    else:
        DP[i] = 1

if DP[N] == 1:
    print("SK")
else:
    print("CY")