N = int(input())

N_list = [0] * 301
for i in range(N):
    N_list[i] = int(input())

A_list = [0] * len(N_list)
A_list[0] = N_list[0]
A_list[1] = N_list[0] + N_list[1]
A_list[2] = max(N_list[0] + N_list[2], N_list[1] + N_list[2])

for i in range(3, N):
    A_list[i] = max(N_list[i-1] + A_list[i-3], A_list[i-2]) + N_list[i]

print(A_list[N-1])