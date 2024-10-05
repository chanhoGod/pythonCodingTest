N = int(input())

N_list = [list(map(int, input().split())) for i in range(N)]

## 현재 단계는 이전 단계의 i, i-1중 큰걸 더해주어서 다시 리스트에 넣는다.
## 마지막에 마지막 리스트에 있는 가장 큰 값을 출력한다.

for i in range(1, N):
    for j in range(0, len(N_list[i])):
        if j == 0:
            N_list[i][j] = N_list[i-1][j] + N_list[i][j]
        elif j == len(N_list[i]) - 1:
            N_list[i][j] = N_list[i-1][j-1] + N_list[i][j]
        else:
            N_list[i][j] = max(N_list[i-1][j], N_list[i-1][j-1]) + N_list[i][j]


print(max(N_list[N-1]))