from collections import deque

N = int(input())

O = deque([i for i in range(1, N+1)])

while O:
    if len(O) == 1:
        print(O[0])
        break
        
    O.popleft()
    idx = O.popleft()
    O.append(idx)

