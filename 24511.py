from collections import deque
import sys

N = int(sys.stdin.readline())

qs_list = list(map(int, sys.stdin.readline().split()))

idx_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

queue_list = deque()

for i in range(0, N):
    if qs_list[i] == 0:
        queue_list.append(idx_list[i])
        

for i in range(M):
    queue_list.appendleft(M_list[i]) 
    othernum = queue_list.pop()
    print(othernum, end=" ")