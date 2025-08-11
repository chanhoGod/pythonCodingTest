N = int(input())

visited = [0] * N


def check_queen(row, col):
    for i in range(row):
        if visited[i] == col or abs(i - row) == abs(visited[i] - col):
            return False
    
    return True


def dfs(row):
    if row == N:
        return 1
    
    count = 0
    for col in range(N):
        if check_queen(row, col):
            visited[row] = col
            count += dfs(row + 1)
    
    return count


print(dfs(0))