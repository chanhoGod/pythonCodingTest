from itertools import permutations

N, M = map(int, input().split())
A = list(map(int, input().split()))

result = 0

for per in permutations(A):
    tmp = 0
    for i in range(N-2):
        tmp = per[i] + per[i+1] + per[i+2]
        if tmp <= M:
            result = max(result, tmp)

print(result)