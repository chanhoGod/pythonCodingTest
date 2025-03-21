from collections import deque
N, K = map(int,input().split())
visited = [False] * 100002
def dfs(val):
    
    A = deque()
    A.append((val, 0))
    
    while len(A) > 0:
        num, depth = A.popleft()
        if num != K:
            if visited[num] == False:
                visited[num] = True
                if num - 1 >= 0:
                    A.append((num-1, depth+1))
                if num + 1 <= 100001:
                    A.append((num+1, depth+1))
                if num * 2 <= 100001:
                    A.append((num*2, depth+1))
        else:
            print(depth)
            break

dfs(N)