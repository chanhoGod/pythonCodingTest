import sys
from collections import deque

read = sys.stdin.readline

N, M = map(int, read().strip().split())

A = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, read().strip().split())
    A[a].append(b)

visited_list = [False] * (N+1)
check_list = [0] * (N+1)

def bfs(start):
    B = deque()
    B.append(start)
    visited_list[start] = True
    
    while B:
        idx = B.popleft()
        for i in A[idx]:
            if visited_list[i] == False:
                check_list[i] += 1
                visited_list[i] = True
                B.append(i)


for i in range(1, N+1):
    visited_list = [False] * (N+1)
    bfs(i)
    

maxVal = 0
for i in range(1, N+1):
    if check_list[i] > maxVal:
        maxVal = check_list[i]

for i in range(1, N+1):
    if check_list[i] == maxVal:
        print(i, end=' ')