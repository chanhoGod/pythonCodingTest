K, N = map(int, input().split())

O = [0] * (K+1)

for i in range(1, K+1):
    O[i] = int(input())

start = 1
end = max(O)
result = 0

while start <= end:
    mid = (start + end) // 2
    
    maxval = mid
    sumval = 0
    for j in range(1, K+1):
        sumval += O[j] // maxval
    
    if sumval < N:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)