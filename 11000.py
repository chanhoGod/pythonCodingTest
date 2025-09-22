import sys
import heapq
read = sys.stdin.readline

N = int(read())
O = []
for i in range(N):
    a, b = map(int, read().split())
    O.append((a, b))
O = sorted(O, key=lambda x:x[0])

result = 0
last_time_list = []
heapq.heapify(last_time_list)

for a, b in O:

    if last_time_list and last_time_list[0] <= a:
        heapq.heappop(last_time_list)
    else:
        result += 1
    
    heapq.heappush(last_time_list, b)

print(result)