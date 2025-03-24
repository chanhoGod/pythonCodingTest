N = int(input())

O = []

A = list(map(int, input().split()))
O = [0] + A

M = int(input())

start = 0
end = max(O)
result = 0
while start <= end:
    mid = (start + end) // 2
    
    sumval = 0
    for i in range(1, N+1):
        sumval += min(mid, O[i])
    
    if sumval > M:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)