import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, read().strip().split())

O = []
U = [i for i in range(V+1)]
C = [0 for i in range(V+1)]

for i in range(1, E+1):
    a, b, c = map(int, read().strip().split())
    O.append((a, b, c))

def find(val):
    if U[val] != val:
        U[val] = find(U[val])
        return U[val]
    else:
        return val
    
    
def union(a, b, c):
    a = find(a)
    b = find(b)
    
    if a != b:
        U[b] = a
        C[b] = C[a] + c
    
# 최소신장트리
# 1. 간선을 가중치에 따라 오름차순으로 정렬
# 2. 가장 작은 가중치를 가진 간선부터 연결
# 3. 사이클이 생기지 않도록 조심
# 4. 모든 정점이 연결될 때까지 반복

# 1.
O.sort(key=lambda x: x[2])

# 2.
for i in range(E):
    a, b, c = O[i]
    
    if find(a) != find(b):
        union(a, b, c)
    else:
        continue

print(sum(C))