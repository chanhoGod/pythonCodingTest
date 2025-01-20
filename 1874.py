import sys

read = sys.stdin.readline

N = int(read().strip())

D = list()
R = list()

idx = 1

for i in range(N):
    num = int(read().strip())
    
    if idx <= num:
        for j in range(idx, num + 1):
            D.append(j)
            R.append('+')
            idx += 1

    pop_num = D.pop()
    
    if pop_num == num:
        R.append('-')
    else:
        R.clear()
        break

if len(R) > 0:
    for i in R:
        print(i)
else:
    print('NO')