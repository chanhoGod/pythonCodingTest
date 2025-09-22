import sys

read = sys.stdin.readline

M, N = map(int, read().split())
O = list(map(int, read().split()))
start = 1
end = max(O)
result = 0

def list_sub(mid):
    cnt = 0
    for i in O:
        cnt += i//mid
    
    return cnt

while start <= end:
    mid = (start + end)//2
    
    cookie_cnt = list_sub(mid)
    
    if cookie_cnt >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
    
print(result)