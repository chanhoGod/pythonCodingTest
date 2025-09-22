X, Y = map(int, input().split())


Z = int(Y * 100 / X)

if Z == 99:
    print(-1)
    exit()

start = 1
end = 1000000000
result = -1
while start <= end:
    mid = (start + end)//2
    
    new_rate = int((Y + mid) * 100 / (X + mid))
    
    if new_rate > Z:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)