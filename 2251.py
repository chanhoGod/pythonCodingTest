import sys
from collections import deque

read = sys.stdin.readline

A, B, C = map(int, read().split())

visited = [[False] * (B + 1) for i in range(A + 1)]

queue = deque()
queue.append((0, 0))
visited[0][0] = True

result = list()

def visited_check(x, y):
    if visited[x][y] == False:
        visited[x][y] = True
        queue.append((x, y))

def bfs():
    while queue:
        x, y = queue.popleft()
        z = C - x - y
        
        if x == 0:
            result.append(z)

        # A -> B
        w = min(x, B - y)
        visited_check(x - w, y + w)
        
        # B -> A
        w = min(A - x, y)
        visited_check(x + w, y - w)

        # A -> C
        w = min(x, C - z)
        visited_check(x - w, y)

        # C -> A
        w = min(A - x, z)
        visited_check(x + w, y)

        # B -> C
        w = min(y, C - z)
        visited_check(x, y - w)

        # C -> B
        w = min(B - y, z)
        visited_check(x, y + w)

bfs()
result.sort()

print(*result)