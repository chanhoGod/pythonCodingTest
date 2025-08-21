import sys

read = sys.stdin.readline

N = int(read())

O = list(map(int, read().split()))
M = int(read())

start = 1
end = max(O)
result = 0
def can_make(mid):
    
    cnt = 0
    for i in range(N):
        idx = O[i]
        if idx <= mid:
            cnt += idx
        else:
            cnt += mid
    
    return cnt

while start <= end:
    mid = (start + end) // 2
    
    tmp_cnt = can_make(mid)
    if tmp_cnt > M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)