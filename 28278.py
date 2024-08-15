import sys

def check_stack_size(input_stack):
    if len(input_stack) == 0:
        print(1)
    else:
        print(0)

N = int(sys.stdin.readline().strip())

stack = list()

for i in range(N):
    numlist = list(map(int, sys.stdin.readline().split()))
    
    C = numlist[0]
    M = numlist[1] if len(numlist) > 1 else 0
    
    if C == 4:
        check_stack_size(stack)
    elif C == 1:
        stack.append(M)
    elif C == 3:
        print(len(stack))
    elif C == 2:
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif C == 5:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    