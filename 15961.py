import sys
from collections import deque
read = sys.stdin.readline

N, D, K, C = map(int, read().split())

O = [int(read()) for _ in range(N)]
TD = dict()
result = 0
idx = 0

for i in range(K):
    new_plate = O[i]
    
    if new_plate not in TD:
        TD[new_plate] = 1
        idx += 1
    else:
        TD[new_plate] += 1

if C not in TD:
    TD[C] = 1
    idx += 1

for i in range(K, N + K):
    new_plate = O[i%N]
    old_plate = O[i - K]
    
    if new_plate not in TD:
        TD[new_plate] = 1
        idx += 1
    else:
        TD[new_plate] += 1
    
    if old_plate in TD:
        TD[old_plate] -= 1
        if TD[old_plate] == 0:
            del TD[old_plate]
            idx -= 1
        
    if C not in TD:
        TD[C] = 1
        idx += 1
        
    result = max(result, idx)

print(result)