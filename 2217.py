import sys

read = sys.stdin.readline

N = int(read())
O = [int(read()) for _ in range(N)]

O.sort(reverse=True)
result = 0

for i in range(len(O)):
    tmp = O[i] * (i+1)
    result = max(result, tmp)

print(result)