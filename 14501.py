N = int(input())

DP = [0] * (N + 2)
T = [0] * (N + 2)
P = [0] * (N + 2)

for i in range(1, N+1):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

for i in range(N, 0, -1):
    if i + T[i] > N + 1:
        DP[i] = DP[i+1]
    else:
        DP[i] = max(DP[i+1], DP[i + T[i]] + P[i])

print(DP[1])