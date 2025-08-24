import sys
from queue import PriorityQueue

read = sys.stdin.readline

T = int(read())

for _ in range(T):
    max_queue = PriorityQueue()
    min_queue = PriorityQueue() 
    D = dict()
    K = int(read())
    for _ in range(K):
        O = read().strip().split()
        A = O[0]
        N = int(O[1])
        
        if A == 'D':
            if max_queue.empty():
                continue
            else:
                if N == 1:
                    while not max_queue.empty():
                        idx = max_queue.get()
                        if D[idx[1]] > 0:
                            D[idx[1]] -= 1
                            break
                        
                elif N == -1:
                    while not min_queue.empty():
                        idx = min_queue.get()
                        if D[idx[1]] > 0:
                            D[idx[1]] -= 1
                            break
        elif A == 'I':
            if N not in D:
                D[N] = 1
            else:
                D[N] += 1
            max_queue.put((-N, N))
            min_queue.put((N, N))
    
    if sum(D.values()):
        print('EMPTY')
    else:
        max_num = 0
        min_num = 0
        
        while not max_queue.empty():
            max_num = max_queue.get()
            if D[max_num[1]] > 0:
                break
        
        while not min_queue.empty():
            min_num = min_queue.get()
            if D[min_num[1]] > 0:
                break
        
        print(max_num[1], min_num[1])
    
