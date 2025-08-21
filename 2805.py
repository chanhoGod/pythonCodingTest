import sys


read = sys.stdin.readline

N, M = map(int, read().split())

O = list(map(int, read().split()))

start = 0
end = max(O)
result = 0
while start <= end:
    mid = (start + end) // 2
    
    k = lambda x: sum((o - x) for o in O if o > x)
    
    sum_height = k(mid)
    if sum_height >= M:
        start = mid + 1
        result = mid
    else:
        end = mid - 1


print(result)