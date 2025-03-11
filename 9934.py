import sys

read = sys.stdin.readline

K = int(read())

O = [[] for i in range(K+1)]

A = list(map(int, read().split()))

root = A[int(len(A)/2)]

def dfs(start, end, depth):
    if start == end:
        O[depth].append(A[start])
        return
    
    mid = int((start + end) / 2)
    
    O[depth].append(A[mid])
    
    dfs(start, mid-1, depth+1)
    dfs(mid+1, end, depth+1)

dfs(0, len(A)-1, 1)

for i in range(1, len(O)):
    print(*O[i])