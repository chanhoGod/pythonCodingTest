import math

N, M = map(int, input().split())

A = [0] * (M+1)

for i in range(2, M+1):
    A[i] = i

for i in range(2, M+1):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0 and i != j:
            A[i] = 0
            break
            
for i in A:
    if i != 0 and i >= N:
        print(i)
