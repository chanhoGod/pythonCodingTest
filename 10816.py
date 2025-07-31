import sys

read = sys.stdin.readline

N = int(read())
N_list = list(map(int, read().split()))

M = int(read())
M_list = list(map(int, read().split()))
M_dict = {key:0 for key in M_list}


for n in N_list:
    if n in M_dict:
        M_dict[n] += 1


for m in M_list:
    print(M_dict[m], end=' ')