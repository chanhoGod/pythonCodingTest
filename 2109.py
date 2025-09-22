import sys
import heapq

read = sys.stdin.readline

N = int(read())
O = [list(map(int, read().split())) for _ in range(N)]
O = sorted(O, key=lambda x: (-x[1], -x[0]))
node_list = []
heapq.heapify(node_list)

result = 0
while O:
    pay, now = O.pop()
    
    if len(node_list) < now:
        heapq.heappush(node_list, pay)
    else:
        if node_list[0] < pay:
            heapq.heappop(node_list)
            heapq.heappush(node_list, pay)

print(sum(node_list))