import sys, math

read = sys.stdin.readline

N = int(read().strip())

O = []
U = [i for i in range(N+1)]
A = []
C = [0 for i in range(N+1)]

for i in range(N):
    a, b = map(float, read().strip().split())
    O.append((a, b))

for i in range(N):
    for j in range(N):
        if i != j:
            A.append((i, j, round(math.sqrt(math.pow(abs(O[i][0] - O[j][0]), 2) + math.pow(abs(O[i][1] - O[j][1]), 2)), 2)))

A.sort(key=lambda x: x[2])

def find(val):
    if U[val] != val:
        U[val] = find(U[val])
        return U[val]
    return val

def union(a, b, c):
    a = find(a)
    b = find(b)
    
    if a != b:
        U[b] = a
        C[b] = C[a] + c
        
for i in range(len(A)):
    a, b, c = A[i]
    if find(a) != find(b):
        union(a, b, c)

print(sum(C))