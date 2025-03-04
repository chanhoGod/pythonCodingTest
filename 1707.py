import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(read())
isYes = True

def dfs(start):
    global isYes
    visited_list[start] = True
    
    for i in A[start]:
        if visited_list[i] == False:
            check_list[i] = (check_list[start] + 1) % 2
            if dfs(i) == False:
                return False
            
        elif check_list[i] == check_list[start]:
            isYes = False
            return False
    
    return True
            

# 방문한 간선에 다시 방문하지 않고 dfs를 통과하는 경우가 있을 경우 YES
for i in range(N):
    V, E = map(int, read().split())

    #정점 리스트 생성
    A = [[] for _ in range(V + 1)]
    visited_list = [False] * (V + 1)
    check_list = [0] * (V + 1)

    #정점 리스트에 간선 추가
    for i in range(E):
        a, b = map(int, read().split())
        
        A[a].append(b)
        A[b].append(a)

    isYes = True
    for i in range(1, len(A)):
        if isYes == True:
            dfs(i)
        else:
            print('NO')
            break
        
    if isYes == True:
        print('YES')