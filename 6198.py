import sys
read = sys.stdin.readline

N = int(read())
O = [int(read()) for i in range(N)]

stack = []
result = 0
for idx in O:
    
    while stack and stack[-1] <= idx:
        stack.pop()
    
    result += len(stack)
    stack.append(idx)

print(result)