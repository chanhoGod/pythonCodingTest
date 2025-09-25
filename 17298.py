import sys

read = sys.stdin.readline

N = int(read())
O = list(map(int, read().split()))

stack = []
result = [0] * N
for i, idx in enumerate(O, start=0):
    while stack and stack[-1][1] < idx:
        si, sdx = stack.pop()
        result[si] = idx
    
    stack.append((i, idx))

for i, idx in enumerate(result):
    if result[i] == 0:
        result[i] = -1

print(*result)