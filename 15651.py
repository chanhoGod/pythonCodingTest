def dfs():
    if len(A) == M:
        print(' '.join(map(str,A)))
        return 
    
    for i in range(1, N + 1):
        A.append(i)
        dfs()
        A.pop()
        
        

N, M = map(int, input().split())

A = []
dfs()