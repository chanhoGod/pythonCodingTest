import sys
from queue import PriorityQueue

read = sys.stdin.readline

N = int(read())

A = [[0]*2 for i in range(N)]

for i in range(N):
    start, end = map(int, read().strip().split())
    
    A[i][0] = end
    A[i][1] = start

A.sort()
count = 0
endtime = 0

for i in range(N):
    if A[i][1] >= endtime:
        endtime = A[i][0]
        count += 1

print(count)


