import sys

read = sys.stdin.readline

N, M = map(int, read().strip().split())

N_list = list(map(int, list(read().strip().split())))

sum_list = list()
sum_list.append(N_list[0])

for i in range(1, len(N_list)):
    sum_list.append(sum_list[i-1] + N_list[i])

for i in range(M):
    n, m = map(int, read().strip().split()) 
    A = sum_list[n-2] if n > 1 else 0
    B = sum_list[m-1]
    print(B - A)