import sys

read = sys.stdin.readline

N, M = map(int, read().split())

N_set = set(read().strip() for i in range(N))
M_set = set(read().strip() for i in range(M))

answer = sorted(N_set & M_set)

print(len(answer))
print('\n'.join(answer))