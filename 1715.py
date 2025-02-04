import sys
from queue import PriorityQueue

read = sys.stdin.readline

N = int(read().strip())

A = PriorityQueue()
for i in range(N):
    idx = int(read().strip())
    A.put(idx)

deck = 0

while A.qsize() > 1:
    dummy1 = A.get()
    dummy2 = A.get()
    k = dummy1 + dummy2
    deck += k
    A.put(k)
    
print(deck)