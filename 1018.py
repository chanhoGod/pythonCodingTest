def board_check(board, color_type):

    now_board_color_type = color_type
    min_count = 0

    if color_type == "B":
        for i in range(0, 8):
            for j in range(0, 8):
                if board[i][j] == now_board_color_type:
                    if now_board_color_type == "B":
                        now_board_color_type = "W"
                    elif now_board_color_type == "W":
                        now_board_color_type = "B"
                else:
                    if now_board_color_type == "B":
                        now_board_color_type = "W"
                    elif now_board_color_type == "W":
                        now_board_color_type = "B"
                    min_count += 1
                    
            if now_board_color_type == "B":
                now_board_color_type = "W"  
            elif now_board_color_type == "W":
                now_board_color_type = "B"
    
    elif color_type == "W":
        for i in range(0, 8):
            for j in range(0, 8):
                if board[i][j] == now_board_color_type:
                    if now_board_color_type == "B":
                        now_board_color_type = "W"
                    elif now_board_color_type == "W":
                        now_board_color_type = "B"
                else:
                    if now_board_color_type == "B":
                        now_board_color_type = "W"
                    elif now_board_color_type == "W":
                        now_board_color_type = "B"
                    min_count += 1
            
            if now_board_color_type == "B":
                now_board_color_type = "W"  
            elif now_board_color_type == "W":
                now_board_color_type = "B"



    return min_count
    
N, M = map(int, input().split())

board_arr = list()

min_change_num = 2501

# 전체 보드 입력 
for i in range(N):
    board_arr.append(list(input()))

eight_board = list()

for i in range(0, N - 7):
    for j in range(0, M - 7):
        eight_board = [row[j:j+8] for row in board_arr[i:i+8]]
        b_count = board_check(eight_board, "B")
        w_count = board_check(eight_board, "W")
        
        tmp_min_cnt = min(b_count, w_count)
        if min_change_num > tmp_min_cnt:
            min_change_num = tmp_min_cnt
        
print(min_change_num)