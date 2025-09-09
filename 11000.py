import sys
import heapq

read = sys.stdin.readline

N = int(read())
O = sorted([list(map(int, read().split())) for _ in range(N)], key=lambda x:x[0])

min_end = []
heapq.heapify(min_end)
result = 0

for i in O:
    start, end = i
    
    if min_end and min_end[0] <= start:
        heapq.heappop(min_end)
    else:
        result += 1
    heapq.heappush(min_end, end)


print(result)