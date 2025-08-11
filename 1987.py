import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**5)

R, C = map(int, read().split())

target_list = [list(map(str, read().strip())) for _ in range(R)]
visited = set() 

result = 1

def dfs(sx, sy, cnt):
    global result
    result = max(result, cnt)
    
    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + sx, y + sy
        
        if 0 <= nx < R and 0 <= ny < C:
            next_point = target_list[nx][ny]
            if next_point not in visited:
                visited.add(next_point)
                dfs(nx, ny, cnt + 1)
                visited.remove(next_point)

visited.add(target_list[0][0])
dfs(0, 0, 1)

print(result)