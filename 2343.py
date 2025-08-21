N, M = map(int, input().split())

O = list(map(int, input().split()))


start = max(O)
end = sum(O)
result = 0

def can_install(mid):
    m = 1
    tmp_cnt = 0
    for i in range(N):
        tmp_cnt += O[i]
        if tmp_cnt <= mid:
            continue
        else:
            m += 1
            tmp_cnt = O[i]
            if m > M:
                return False
    
    return m <= M

while start <= end:
    mid = (start + end) // 2
    
    if can_install(mid):
        result = mid
        end = mid - 1
    else:
        start = mid + 1
        
        
print(result)
