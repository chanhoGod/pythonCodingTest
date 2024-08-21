from collections import deque 
import sys

N = int(input())

num_queue = deque()

for i in range(N):
    str = sys.stdin.readline()
    
    num_arr = list(map(int, str.split()))
    
    A = num_arr[0]
    X = num_arr[1] if len(num_arr) > 1 else 0
    
    if A == 1:
        num_queue.appendleft(X)
    elif A == 2:
        num_queue.append(X)
    elif A == 3:
        if len(num_queue) > 0:
            print(num_queue.popleft())
        else:
            print(-1)
    elif A == 4:
        if len(num_queue) > 0:
            print(num_queue.pop())
        else:
            print(-1)
    elif A == 5:
        print(len(num_queue))
    elif A == 6:
        if len(num_queue) > 0:
            print(0)
        else:
            print(1)
    elif A == 7:
        if len(num_queue) > 0:
            print(num_queue[0])
        else:
            print(-1)
    elif A == 8:
        if len(num_queue) > 0:
            print(num_queue[-1])
        else:
            print(-1)