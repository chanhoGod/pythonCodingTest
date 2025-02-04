import sys


read = sys.stdin.readline


N = int(read().strip())

k = int(read().strip())
A = [[i*j for j in range(1, N+1)] for i in range(1, N+1)]
B = [i for i in A]

start = 1
end = k
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    
    for i in range(1, N+1):
        cnt += min(int(mid // i), N)
    
    if cnt < k:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1
print(answer)
