import math

N, M = map(int, input().split())

A = [0] * (int(math.sqrt(M)) + 1)
for i in range(2, len(A)):
    A[i] = i
    

for i in range(2, int(math.sqrt(M))+1):
    if A[i] != 0:
        for j in range(i*i, int(math.sqrt(M))+1, i):
            A[j] = 0

count = 0

for i in A:
    if i > 0:
        idx = i * i
        while idx <= M:
            if idx > M:
                break
            elif idx < N:
                idx *= i
                continue
            else:
                count += 1
                idx *= i

print(count)