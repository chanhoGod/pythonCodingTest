import sys

read = sys.stdin.readline

N, M = map(int, read().split())
O = list(map(int, read().split()))
start = 0
end = 0

sum_val = 0
result = 0
while start < N:
    if sum_val < M and end < N: 
        sum_val += O[end]
        end += 1
    else:
        if sum_val == M:
            result += 1
        sum_val -= O[start]
        start += 1

print(result)