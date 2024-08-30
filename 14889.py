import sys
input = sys.stdin.readline
N = int(input())

N_list = [list(map(int, input().split())) for _ in range(N)]
check_team = [False for _ in range(N)]
min_num = sys.maxsize

def divide_team(seq, idx):
    global min_num   
    if seq == N // 2:
        a, b = 0, 0
        for i in range(N):
            for j in range(N):
                if check_team[i] and check_team[j]:
                    a += N_list[i][j]
                elif not check_team[i] and not check_team[j]:
                    b += N_list[i][j]
        min_num = min(min_num, abs(a - b))
        return
    
    for i in range(idx, N):
        if not check_team[i]:        
            check_team[i] = True
            divide_team(seq + 1, i + 1)
            check_team[i] = False

divide_team(0, 0)
print(min_num)