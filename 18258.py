from collections import deque
import sys

N = int(input())

number_queue = deque()

for i in range(N):
    str_list = sys.stdin.readline().split()
    
    if len(str_list) > 1:
        key = str_list[0]
        value = int(str_list[1])
        if key == "push":
            number_queue.append(str_list[1])
    else:
        key = str_list[0]
        queue_len = len(number_queue)
        if key == "pop":
            if queue_len >= 1:
                pop = number_queue.popleft()
                print(pop)
            else:
                print(-1)
        elif key == "front":
            if queue_len >= 1:
                print(number_queue[0])
            else:
                print(-1)
        elif key == "back":
            if queue_len >= 1:
                print(number_queue[-1])
            else:
                print(-1)
        elif key == "empty":
            if queue_len >= 1:
                print(0)
            else:
                print(1)
        elif key == "size":
            print(queue_len)