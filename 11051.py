N, K = map(int, input().split())

O = [[0] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    O[i][0] = 1
    O[i][1] = i
    O[i][i] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        O[i][j] = (O[i-1][j-1] + O[i-1][j]) % 10007

print(O[N][K])