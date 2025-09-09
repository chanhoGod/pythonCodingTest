import sys

read = sys.stdin.readline

T = int(read())

for _ in range(T):
    
    N = int(read())
    O = [list(map(int, read().split())) for _ in range(N)]
    O.sort(key=lambda x: (x[0], x[1]))
    
    result = 1
    best_i = O[0][1]
    
    for i in range(1, N):
        if O[i][1] < best_i:
            result += 1
            best_i = O[i][1]
    
    print(result)