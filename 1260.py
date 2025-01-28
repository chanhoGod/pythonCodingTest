import sys
from collections import deque

read = sys.stdin.readline

N, M, V = map(int, read().split())

graph = [[] for i in range(N + 1)]
visit_list = []
dfs_list = []
bfs_list = []

for i in range(M):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N + 1):
    graph[i].sort()

def dfs(seq, depth):
    visit_list[seq] = True
    print(seq, end=' ')
    
    for i in graph[seq]:
        if visit_list[i] == False:
            dfs(i, depth+1)
    

visit_list = [False] * (N + 1)
dfs(V, 1)

print()


def bfs(seq):
    queue = deque()
    queue.append(seq)
    # bfs_list.append(seq)
    print(seq, end=' ')
    visit_list[seq] = True
    
    while queue:
        leftpop = queue.popleft()
        for i in graph[leftpop]:
            if visit_list[i] == False:
                # bfs_list.append(i)
                print(i, end=' ')
                queue.append(i)
                visit_list[i] = True

visit_list = [False] * (N + 1)
bfs(V)