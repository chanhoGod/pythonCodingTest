import sys

read = sys.stdin.readline

N, M = map(int, read().split())

O = [list(map(int, read().split())) for _ in range(M)]


result = 0
min_package = float('inf')
min_each = float('inf')

for i in O:
    p, e = i
    min_package = min(min_package, p)
    min_each = min(min_each, e)

result = min((N//6) * min_package + (N%6) * min_each, N * min_each, (N//6) * min_package + min_package)

print(result)