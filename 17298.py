import sys

read = sys.stdin.readline

N = int(read())

O = list(map(int, read().split()))
stack = list()
result = [-1] * N
for i in range(N):
    while stack and O[stack[-1]] < O[i]:
        idx = stack.pop()
        result[idx] = O[i]
    
    stack.append(i)

print(*result)    