from collections import deque

N = int(input())

ballon_list = deque(enumerate(map(int, input().split()), start=1))


for i in range(N):
    paper = ballon_list.popleft()
    
    print(paper[0], end = ' ')
    
    if paper[1] > 0:
        ballon_list.rotate(-(paper[1] - 1))
    else:
        ballon_list.rotate(-paper[1])