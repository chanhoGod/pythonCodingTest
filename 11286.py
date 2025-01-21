from queue import PriorityQueue
import sys

read = sys.stdin.readline

N = int(read().strip())

A = PriorityQueue()

for i in range(N):
    idx = int(read().strip())
    
    if idx == 0:
        if A.empty():
            print('0')
        else:
            print(A.get()[1])
    else:
        A.put((abs(idx), idx))
        
