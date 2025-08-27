import sys

read = sys.stdin.readline

N, K = map(int, read().split())
O = list(map(int, read().split()))

start = 0
end = 0
D = dict()
result = 0

while end < N:
    idx = O[end]
    if idx not in D:
        D[idx] = 1
    else:
        D[idx] += 1
    if D[idx] > K:
        while D[idx] > K:
            delete_value = O[start]
            D[delete_value] -= 1
            start += 1
    
    result = max(result, end - start + 1)
    end += 1

print(result)