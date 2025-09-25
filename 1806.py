import sys

read = sys.stdin.readline

N, K = map(int, read().split())

O = list(map(int, read().split()))


result = float('inf')

start = 0
end = 0
sum_val = 0
while end < N:
    sum_val += O[end]
    
    while sum_val >= K:
        result = min(result, end - start + 1)
        sum_val -= O[start]
        start += 1
    end += 1
    

if result == float('inf'):
    print(0)
else:
    print(result)
