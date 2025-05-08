import sys

read = sys.stdin.readline

N, M = map(int, read().split())

O = [0] + list(map(int, read().split()))
A = [0] * (N+1)
A[0] = O[0]

max_num = -100000000
for i in range(1, N+1):
    A[i] = O[i] + A[i-1]

for i in range(M, N+1):
    value = A[i] - A[i-M]
    if max_num < value:
        max_num = value

# print(A)
print(max_num)