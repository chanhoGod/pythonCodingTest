from collections import deque
import sys

read = sys.stdin.readline

N, M, K, X = map(int, read().split())

A = [[] for _ in range(N+1)]

for i in range(1, M+1):
    a, b = map(int, read().split())
    A[a].append(b)

checklist = [-1] * (N+1)

def bfs(start):
    B = deque()
    B.append(start)
    checklist[start] += 1
    
    while B:
        idx = B.popleft()

        for i in A[idx]:
            if checklist[i] == -1:
                B.append(i)
                checklist[i] = checklist[idx] + 1
        

bfs(X)

answer = []

for i in range(N+1):
    if checklist[i] == K:
        answer.append(i)

answer.sort()

if answer:
    for i in answer:
        print(i)
else:
    print(-1)