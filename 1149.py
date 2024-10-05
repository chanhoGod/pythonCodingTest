N = int(input())

N_list = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    N_list[i][0] = min(N_list[i-1][1], N_list[i-1][2]) + N_list[i][0]
    N_list[i][1] = min(N_list[i-1][0], N_list[i-1][2]) + N_list[i][1]
    N_list[i][2] = min(N_list[i-1][0], N_list[i-1][1]) + N_list[i][2]
    
print(min(N_list[N-1][0], N_list[N-1][1], N_list[N-1][2]))