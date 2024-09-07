def dfs(a):
    if len(A) == M:
        print(' '.join(map(str, A)))
        return

    for i in range(a, N + 1):
        A.append(i)
        dfs(i)
        A.pop()

N, M = map(int, input().split())

A = []

dfs(1)