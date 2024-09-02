N = 9
origin_board = [list(map(int, input().split())) for _ in range(N)]

#세로줄 확인
def col_check(n, col_num):
    for i in range(N):
        if origin_board[i][col_num] == n:
            return False
        
    return True

#가로줄 확인
def row_check(n, row_num):
    if n in origin_board[row_num]:
        return False
    
    return True

# 3X3 확인
def square_check(n, row_num, col_num):
    for i in range(row_num, row_num + (row_num % 3) + 1):
        for j in range(col_num, col_num + (col_num % 3) + 1):
            if origin_board[i][j] == n:
                return False
            
    return True


def dfs(row, col):
    if row == 9 and col == 9:
        return
    
    if col == 9:
        col = 0
        row += 1
    
    for i in range(1, 10):
        if col_check(i, col) and row_check(i, row) and square_check(i, row, col):
            continue
        
        dfs(row)
                
    
    


dfs()