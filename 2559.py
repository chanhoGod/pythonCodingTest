import sys

read = sys.stdin.readline

N, K = map(int, read().split())

O = list(map(int, read().split()))

result = sum(O[:K])
now = result
for i in range(len(O) - K):
    start = O[i]
    end = O[i+K]
    now -= start
    now += end
    
    result = max(result, now)

print(result)