## 기수정렬로 구현

import sys

read = sys.stdin.readline

N = int(read())
max_num = 10000

A = [0] * (max_num + 1)

for i in range(N):
    idx = int(read())
    
    A[idx] += 1

start = 1
while start < 10001:
    if A[start] > 0:
        print(start)
        A[start] -= 1
    else:
        start += 1
