import sys

N = int(sys.stdin.readline().strip())
N_list = list(map(int, sys.stdin.readline().strip().split()))

N_dict = {key:0 for key in N_list}

for i in N_list:
    N_dict[i] += 1

M = int(sys.stdin.readline().strip())
M_list = list(map(int, sys.stdin.readline().strip().split()))

for i in range(0, len(M_list)):
    if M_list[i] in N_dict:
        M_list[i] = N_dict[M_list[i]]
    else:
        M_list[i] = 0

print(*M_list)