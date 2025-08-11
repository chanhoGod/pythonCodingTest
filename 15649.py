import sys

read = sys.stdin.readline

N, M = map(int, read().split())

visited = [False] * (N+1)
target_list = []
def dfs(depth):
    if depth == M:
        print(*target_list)
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            target_list.append(i)
            visited[i] = True
            dfs(depth+1)
            visited[i] = False
            target_list.pop()

dfs(0)