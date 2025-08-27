N = int(input())

D = [0] * (N +1)

D[1] = 1

if N >= 2:
    D[2] = 2

for i in range(3, N+1):
    D[i] = (D[i-1] + D[i-2]) % 15746

print(D[N])