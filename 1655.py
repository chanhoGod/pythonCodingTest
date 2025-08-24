import sys
import heapq
read = sys.stdin.readline

N = int(read())
max_heap = []  
min_heap = [] 

for i in range(1, N+1):
    idx = int(read())
    
    if not max_heap or idx < -max_heap[0]:
        heapq.heappush(max_heap, -idx)
    else:
        heapq.heappush(min_heap, idx)
    
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    
    print(-max_heap[0])