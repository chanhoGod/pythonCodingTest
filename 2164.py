import sys
from collections import deque

read = sys.stdin.readline

N = int(read().strip())

A = deque(i for i in range(1, N + 1))

flag = True

while len(A) > 1:
    if flag:
        A.popleft()
        flag = False
    else:
        A.append(A.popleft())
        flag = True


print(A[0])