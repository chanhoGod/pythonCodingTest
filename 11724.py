import sys


read = sys.stdin.readline

N, M = map(int, read().split())

visitlist = [False] * (N + 1)
checkstack = list()
resultlist = list()
graph = [[] for _ in range(N + 1)]


for i in range(M):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

## 그래프가 연결되어 있는 값이 있을때는 스택에서 출력, 없는 경우에는 인덱스에서 값을 가져와서 계산
for i in range(1, N + 1):
    visit_num = 0
    if len(checkstack) > 0:
        visit_num = checkstack.pop()
    else:
        visit_num = i
    
    resultlist.append(visit_num)
    visitlist[visit_num] = True
    for i in graph[visit_num]:
        if visitlist[i] == False:
            checkstack.append(i)
            visitlist[i] = True
    
    if len(checkstack) < 1:
        cnt += 1

print(cnt)