import sys
from queue import PriorityQueue

read = sys.stdin.readline

N, D = map(int, read().strip().split())
O = [i for i in range(D+1)]
L = []

for i in range(N):
    s, e, d = map(int, read().strip().split())
    if e - s > d:
        L.append((s, e, d))

L.sort()

for i in L:
    item = i
    s = item[0]
    e = item[1]
    d = item[2]
    
    for j in range(1, D+1):
        if e == j:
            O[j] = min(O[j], O[s] + d)
        else:
            O[j] = min(O[j], O[j-1] + 1)

print(O[D])
