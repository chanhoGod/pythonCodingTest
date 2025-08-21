K, N = map(int, input().split())

O = [int(input()) for _ in range(K)]

start = 1
end = max(O)
result = 0


while start <= end:
    mid = (start + end) // 2
    
    sum_val = sum(o//mid for o in O if o >= mid)
    
    if sum_val >= N:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
        
print(result)