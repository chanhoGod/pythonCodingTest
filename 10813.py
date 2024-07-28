def change_ball(a, b ,basketArray):
    tmp = basketArray[a - 1]
    basketArray[a - 1] = basketArray[b - 1]
    basketArray[b - 1] = tmp

N, M = map(int, input().split())


basketArray = [0] * N

for i in range(len(basketArray)):
    basketArray[i] = i+1


for i in range(M):
    a, b = map(int, input().split())
    change_ball(a, b ,basketArray)
    
    
    
for i in basketArray:
    print(i, end=' ')