from collections import deque

N = int(input())

O = [[-1] * (N+1) for i in range(N+1)]
visited = [[False] * (N+1) for i in range(N+1)]
for i in range(1, N+1):
    A = list(map(int, input()))
    O[i] = [-1] + A

def bfs(O, x, y):
    B = deque()
    B.append((x, y))
    result = 0
    while len(B) > 0:
        a, b = B.popleft()
        if O[a][b] == 1:
            if visited[a][b] == False:
                visited[a][b] = True
                result += 1
                if b < N:
                    B.append((a, b+1))
                
                if a > 0:
                    B.append((a-1, b))
                
                if a < N:
                    B.append((a+1, b))
                    
                if b > 0:
                    B.append((a, b-1))
    
    return result

answer = list()
for i in range(1, N+1):
    for j in range(1, N+1):
        if visited[i][j] == False:
            a = bfs(O, i, j)
            if a != 0:
                answer.append(a)

answer = sorted(answer)
print(len(answer))
for i in answer:
    print(i)