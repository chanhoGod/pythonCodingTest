T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())

    O = [[j for j in range(N+1)] for i in range(K+1)]

    for i in range(1, K+1):
        for j in range(1, N+1):
            O[i][j] = O[i-1][j] + O[i][j-1] 
    
    print(O[K][N])

