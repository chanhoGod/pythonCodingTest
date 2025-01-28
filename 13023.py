import sys


read = sys.stdin.readline

N, M = map(int, read().split())

checklist = list()
visitlist = [False] * N
graph = [[] for _ in range(N)]


for i in range(M):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

result = False

def dfs(a, depth):
    global result

    if depth == 5:
        result = True
        return
    
    visitlist[a] = True
    
    for i in graph[a]:
        if visitlist[i] == False:
            dfs(i, depth+1)
    
    visitlist[a] = False
    
for i in range(N):
    if result == False:
        dfs(i, 1)
    else:
        break

if result == True:
    print(1)
else:
    print(0)