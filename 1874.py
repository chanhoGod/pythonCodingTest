import sys

read = sys.stdin.readline

N = int(read())
O = list()
result = list()
idx = 1
for i in range(N):
    k = int(read())
    
    for i in range(idx, k+1):
        result.append('+')
        idx += 1
        O.append(i)

    if k == O[-1]:
        result.append('-')
        O.pop()
    else:
        print('NO')
        exit()
    
print('\n'.join(result))