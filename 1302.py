import sys

read = sys.stdin.readline

N = int(read())

D = dict()

for i in range(N):
    S = read().strip()
    
    if S not in D:
        D[S] = 1
    else:
        D[S] += 1

max_val = max(D.values())
result = min(key for key, value in D.items() if value == max_val)
print(result)