import sys

read = sys.stdin.readline


N, M = map(int, read().split())

N_dict = dict(read().split() for _ in range(N))

M_list = list(read() for _ in range(M))

for i in M_list:
    idx = i.strip()
    if idx in N_dict:
        print(N_dict[idx])