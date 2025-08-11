import sys

read = sys.stdin.readline

N, M = map(int, read().split())
target_list = []

def dfs(depth, now):
    if depth == M:
        print(*target_list)
        return
    
    for i in range(now, N+1):
        target_list.append(i)
        dfs(depth + 1, i+1)
        target_list.pop()

dfs(0, 1)