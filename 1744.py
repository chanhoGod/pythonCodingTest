import sys
from queue import PriorityQueue

read = sys.stdin.readline

N = int(read().strip())

A = PriorityQueue()
B = PriorityQueue()

for i in range(N):
    k = int(read().strip())
    
    if k > 0:
        A.put(-k)
    else:
        B.put(k)
    
answer = 0

while A.qsize() > 1:
    g1 = -A.get()
    g2 = -A.get()
    
    if g1 + g2 > g1 * g2:
        answer += (g1 + g2)
    else:
        answer += (g1 * g2)
    
    if A.qsize() == 1:
        g3 = -A.get()
        answer += g3

if A.qsize() == 1:
    answer += -A.get()
    

while B.qsize() > 1:
    g1 = B.get()
    g2 = B.get()
    
    if g1 + g2 > g1 * g2:
        answer += (g1 + g2)
    else:
        answer += (g1 * g2)
    
    if B.qsize() == 1:
        g3 = B.get()
        answer += g3

if B.qsize() == 1:
    answer += B.get()

print(answer)