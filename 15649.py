
def dfs():
    # 배열 내부 값의 카운트가 M일때 반환
    if len(A) == M:
        print(' '.join(map(str, A)))
        return
    
    for i in range(1, N + 1):
        # 이미 방문한 경우 제외
        if visited[i] == True:
            continue
        
        visited[i] = True
        A.append(i)
        dfs()
        A.pop()
        visited[i] = False
        
N, M = map(int, input().split())

A = []
visited = [False] * (N + 1)
dfs()
