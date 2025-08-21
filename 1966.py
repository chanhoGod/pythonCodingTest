import sys
from collections import deque

read = sys.stdin.readline

T = int(read())

for i in range(T):
    
    N, M = map(int, read().split())
    O = list(map(int, read().split()))
    queue = deque((O[i], i)for i in range(len(O)))
    result = list()
    cnt = 1
    while queue:
        now = queue[0]
        
        if now[0] < max(q[0] for q in queue):
            idx = queue.popleft()
            queue.append(idx)
        else:
            idx = queue.popleft()
            if idx[1] == M:
                print(cnt)
                break
            else:
                cnt += 1
        
    