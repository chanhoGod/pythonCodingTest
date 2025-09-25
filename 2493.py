import sys


read = sys.stdin.readline

N = int(read())
O = list(map(int, read().split()))
stack = list()
result = []

for i in range(N):
    while stack and stack[-1][1] < O[i]:
        stack.pop()
    
    if len(stack) == 0:
        result.append(0)
    else:
        result.append(stack[-1][0])
    
    stack.append((i+1, O[i]))
                
print(*result)