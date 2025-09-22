import sys
import heapq

read = sys.stdin.readline

N = int(read())

O = [int(read()) for _ in range(N)]
heapq.heapify(O)

result = 0


while len(O) > 1:
    a = heapq.heappop(O)
    b = heapq.heappop(O)
    
    c = a + b
    result += c
    heapq.heappush(O, c)

print(result)