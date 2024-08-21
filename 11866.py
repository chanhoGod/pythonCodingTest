from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())

num_queue = deque(i for i in range(1, N + 1))

answer_list = list()
base_K = K

while len(num_queue) > 0:
    if len(num_queue) < K:
        base_K = K % len(num_queue) - 1
    else:
        base_K = K - 1
    
    pop_num = num_queue[base_K]
    for i in range(K):
        if len(num_queue) > 0:
            tmp_pop_num = num_queue.popleft()
        
        
        if i == K - 1:
            answer_list.append(tmp_pop_num)
        else:
            num_queue.append(tmp_pop_num)
    
result_str = str(answer_list)
print('<' + result_str.strip("[""]") + '>')