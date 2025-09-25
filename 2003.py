import sys

read = sys.stdin.readline

N, K = map(int, read().split())
O = list(map(int, read().split()))

start = 0
end = 0
sum_val = 0
result = 0

while end < N:
    sum_val += O[end]

    while sum_val > K:
        sum_val -= O[start]
        start += 1
    
    end += 1
    if sum_val == K:
        result += 1


print(result)