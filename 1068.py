import sys

sys.setrecursionlimit(10**6)

read = sys.stdin.readline

N = int(read().strip())
O = list(map(int, read().split()))
K = int(read().strip())

G = [[] for i in range(N)]
visited = [False] * N

for i in range(N):
    if O[i] == -1:
        continue

    G[i].append(O[i])
    G[O[i]].append(i)

result = 0

def dfs(val):
    global result
    
    visited[val] = True
    count = 0
    
    if val == K:
        return
    
    # print(f'val : {val}, len(G[val]) : {len(G[val])}')
    
    for i in G[val]:
        if i != K and not visited[i]:
            count += 1
            dfs(i)
            
    if count == 0:
        result += 1

for i in range(N):
    if O[i] == -1:
        dfs(i)

print(result)