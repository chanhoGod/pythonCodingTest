
# from functools import reduce 

# def get_factorial(N):
#     if N == 0:
#         N = 1
    
#     A = reduce(lambda x, y : x * y, range(1, N+1))
    
#     return A

# T = int(input())
# for i in range(T):
#     K, N = map(int, input().split())

#     print(int(get_factorial(N) / (get_factorial(K) * get_factorial(N - K))))



T = int(input())

D = [[0 for _ in range(31)] for _ in range(31)]
for j in range(1, 31):
    D[1][j] = j    

for j in range(2, 31):
    for k in range(2, 31):
        D[j][k] = D[j][k-1] + D[j-1][k-1]


for i in range(T):
    a, b = map(int, input().split())
    
    print(D[a][b])