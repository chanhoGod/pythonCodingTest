import sys
import heapq

read = sys.stdin.readline
N = int(read())
O = []

for i in range(N):
    num_list = list(map(int, read().split()))
    for num in num_list:
        heapq.heappush(O, num)
        if len(O) > N:
            heapq.heappop(O)    

print(O[0])