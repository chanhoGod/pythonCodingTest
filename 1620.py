import sys

line = sys.stdin.readline()
N, M = map(int, line.split())

N_list = [sys.stdin.readline().strip() for i in range(N)]

name_dict = dict()

idx = 1

for i in N_list:
    name_dict[i] = idx
    name_dict[str(idx)] = i
    
    idx += 1

for i in range(M):
    inputPoke = sys.stdin.readline().strip()
    
    print(name_dict[inputPoke])
