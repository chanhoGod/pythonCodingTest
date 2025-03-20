import sys

read = sys.stdin.readline

N, G = read().split()
N = int(N)
S = set()
O = list()
K = 0

if G == 'Y':
    K = 1
elif G == 'F':
    K = 2
elif G == 'O':
    K = 3
    
result = 0

for i in range(N):
    a = read().strip()
    
    if a in S:
        continue
    else:
        S.add(a)
        O.append(a)
    
    if len(O) == K:
        result += 1
        O.clear()

print(result)