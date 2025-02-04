import sys

read = sys.stdin.readline


N, K = map(int, read().strip().split())

A = [int(read().strip()) for _ in range(N)]

cnt = 0

for i in reversed(A):
    if K >= i:
        div = K // i
        K = K % i
        cnt += div

print(cnt)