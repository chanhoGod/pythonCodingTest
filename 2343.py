import sys

read = sys.stdin.readline

N, M = map(int, read().strip().split())

A = list(map(int, read().strip().split()))

start = max(A)
end = sum(A)

while start <= end:
    mid = (start + end) // 2
    sumValue = 0
    cnt = 0
    
    for i in range(len(A)):
        if sumValue + A[i] > mid:
            cnt += 1
            sumValue = 0
        
        sumValue += A[i]
    
    if sumValue != 0:
        cnt += 1
    
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1

print(start)