import sys

read = sys.stdin.readline

T = int(read())

for _ in range(T):
    
    N = int(read())
    O = sorted([str(read().strip()) for _ in range(N)])
    flag = True
    for i in range(N-1):
        if O[i+1].startswith(O[i]):
            print('NO')
            flag = False
            break
    if flag == True:
        print('YES')