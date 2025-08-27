import sys

read = sys.stdin.readline

N, M = map(int, read().split())
O = sorted([int(read()) for _ in range(N)])

start = 0
end = 1
result = []

while end < N and start < N:
    first = O[start]
    last = O[end]
    K = last - first
    if K >= M:
        result.append(K)
        start += 1
    else:
        end += 1

print(min(result))