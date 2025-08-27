import sys

read = sys.stdin.readline

N, M = map(int, read().split())

O = list(map(int, read().split()))

result = 0
last = O[0]

for i in range(0, M):
    result += O[i]
    
sum_value = result
for i in range(M, N):
    sum_value = sum_value + O[i] - last
    result = max(result, sum_value)
    last = O[i - M + 1]

print(result)