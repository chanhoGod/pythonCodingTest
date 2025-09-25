import sys


read = sys.stdin.readline

while True:
    line = read().rstrip()
    stack = []
    if line == '.':
        break
    flag = True
    for idx in line:
        if idx == '(' or idx == '[':
            stack.append(idx)
        elif idx == ')':
            if len(stack) > 0:
                pop_idx = stack.pop()
                if pop_idx != '(':
                    flag = False
                    break
            else:
                flag = False
                break
        elif idx == ']':
            if len(stack) > 0:
                pop_idx = stack.pop()
                if pop_idx != '[':
                    flag = False
                    break
            else:
                flag = False
                break
        
    if flag and len(stack) == 0:
        print('yes')
    else:
        print('no')
    