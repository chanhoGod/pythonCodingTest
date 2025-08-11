N = int(input())

N_list = [0] *(N+1)

for i in range(2, N+1):
    N_list[i] = N_list[i-1] + 1
    
    if i % 2 ==0:
        N_list[i] = min(N_list[i], N_list[i//2] + 1)
    
    if i % 3 == 0:
        N_list[i] = min(N_list[i], N_list[i//3] + 1)

print(N_list[N])