import sys

read = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int, read().strip().split())

O = [i for i in range(N+1)]

# 1. Union은 a와 b의 대표노드를 find하여 O[b]에 a의 값을 대입해준다.
# 2. Find는 value가 O[value]와 같은 경우를 찾을때까지 재귀함수로 넣어서 노드를 탐색, 찾게되면 반환하고 그 이전 단계의 값들을 전부 대표노드로 변경

def union_value(a, b):
    a = find_value(a)
    b = find_value(b)
    
    if a != b:
        O[b] = a

def find_value(val):
    if val != O[val]:
        O[val] = find_value(O[val])
        return O[val]
    else:
        return val

for i in range(M):
    uf, a, b = map(int, read().strip().split())
    
    if uf == 0:
        union_value(a, b)
    
    elif uf == 1:
        if find_value(a) == find_value(b):
            print("YES")
        else:
            print("NO")
            