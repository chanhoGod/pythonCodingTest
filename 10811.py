N, M = map(int, input().split())


basketArray = list(range(1,N + 1))
# basketArray = list(i for i in range(1, N))


for i in range(M):
    a, b = map(int, input().split())
    basketArray[a-1:b] = basketArray[a-1:b][::-1]

print(*basketArray, end = " ")
    