def dfs(a):
    if len(A) == M:
        print(' '.join(map(str, A)))
        return 
    
    for i in range(a, N + 1):
        if visited[i]:
            continue
        
        visited[i] = True
        A.append(i)
        dfs(i+1)
        A.pop()
        visited[i] = False

N, M = map(int, input().split())


A = []
visited = [False] * (N + 1)
dfs(1)
