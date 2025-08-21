import sys
from collections import deque
read = sys.stdin.readline

N, K = map(int, read().split())
O = deque(range(1, N+1))
result = list()
while O:
    for i in range(0, K-1):
        O.append(O.popleft())
    
    result.append(O.popleft())

print('<' + ', '.join(map(str, result)) + '>')