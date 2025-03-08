import sys

read = sys.stdin.readline

N, M = map(int, read().split()) 

edges = []
W = [sys.maxsize] * (N+1)

# 엣지 리스트 세팅
for i in range(M):
    start, end, cost = map(int, read().split())
    
    edges.append((start, end, cost))
    
# 시작점 초기화
W[1] = 0

# 거리 리스트 세팅
for i in range(N-1):
    for start, end, cost in edges:
        if W[start] != sys.maxsize and W[end] > W[start] + cost:
            W[end] = W[start] + cost
            
#음수 사이클 확인
mCycle = False

for start, end, cost in edges:
    if W[start] != sys.maxsize and W[end] > W[start] + cost:
        mCycle = True

if not mCycle:
    for i in range(2, N+1):
        if W[i] == sys.maxsize:
            print(-1)
        else:
            print(W[i])
else:
    print(-1)