from collections import deque
N = int(input())

A = [list() for _ in range(N)]
visited = [False] * N
weight_list = [0] * N

for i in range(N):
    a = deque(map(int, input().split()))
    idx = a.popleft()
    
    while a:
        if len(a) > 2:
            x = a.popleft()
            y = a.popleft()
            A[idx-1].append((x, y))
        else:
            break

# print(A)

def bfs(start):
    queue = deque()

    queue.append(start-1)
    visited[start-1] = True
    
    while queue:
        now_node = queue.popleft()
        
        for i in A[now_node]:
            x = i[0]-1
            y = i[1]
            if not visited[x]:
                # print(i)
                weight_list[x] = weight_list[now_node] + y
                visited[x] = True
                queue.append(x)

bfs(1)
maxnum = 0
for i in range(1, N):
    if weight_list[i] > weight_list[maxnum]:
        maxnum = i

visited = [False] * N
weight_list = [0] * N

bfs(maxnum + 1)
print(max(weight_list))


# bfs(5)
# print(weight_list)
# print(max(weight_list))