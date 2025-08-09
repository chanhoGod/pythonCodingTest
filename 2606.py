import sys

read = sys.stdin.readline

N = int(read().strip())
M = int(read().strip())

N_list = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, read().strip().split())
    N_list[a].append(b)
    N_list[b].append(a)

visited = [False] * (N+1)
count = 0
def dfs(node, visited):
    visited[node] = True
    global count
    count += 1
    for i in N_list[node]:
        if not visited[i]:
            dfs(i, visited)
    
dfs(1, visited)
print(count - 1)