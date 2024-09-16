import sys
N = int(input())

N_list = list(map(int, input().split()))

for i in range(1, N):
    N_list[i] = max(N_list[i], N_list[i] + N_list[i-1])
    
    
print(max(N_list))
