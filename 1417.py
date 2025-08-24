import sys
import heapq

read = sys.stdin.readline

N = int(read())

Q = []
result = 0
idx = int(read())
for i in range(2, N+1):
    num = int(read())
    heapq.heappush(Q, -num)

while Q:
    target = -heapq.heappop(Q)
    
    if idx <= target:
        idx += 1
        target -= 1
        result += 1
        heapq.heappush(Q, -target)
    else:
        break
    
print(result)