import sys

read = sys.stdin.readline

N = int(read())


for i in range(N):
    O = list(read().strip())
    rtn = 0
    while O:
        idx = O.pop(0)
        if rtn < 0:
            break
        
        if idx == ')':
            rtn -= 1
        else:
            rtn += 1
    
    print('YES' if rtn == 0 else 'NO')
    