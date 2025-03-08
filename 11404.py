import sys

read = sys.stdin.readline

N = int(read().strip())

M = int(read().strip())

O = [[sys.maxsize for i in range(N+1)] for j in range(N+1)]

for i in range(N+1):
    for j in range(N+1):
        if i == j:
            O[i][j] = 0

for i in range(M):
    a, b, c = map(int, read().strip().split())
    # 노선이 하나가 아니기 때문에 가장 최소의 값으로 저장
    if O[a][b] > c:
        O[a][b] = c
    
# 플로이드-워셜 알고리즘
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            O[i][j] = min(O[i][j], O[i][k] + O[k][j])


for i in range(1, N+1):
    for j in range(1, N+1):
        if O[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(O[i][j], end=' ')
    
    print()