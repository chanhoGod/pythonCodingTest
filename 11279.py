from queue import PriorityQueue
import sys

read = sys.stdin.readline

N = int(read())
queue = PriorityQueue()

for i in range(N):
    
    x = int(read())
    
    if x == 0:
        if queue.empty():
            print(0)
        else:
            key, value = queue.get()
            print(value)
    else:
        queue.put((-x, x))