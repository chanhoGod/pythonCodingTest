N = int(input())
all_coin_array = list()

for i in range(N):
    cost = int(input())
    remainder = 0
    coin_array = [0, 0 ,0 ,0]
    
    while cost > 0:
        if cost >= 25:
            quot = cost // 25
            cost = cost % 25
            coin_array[0] += quot
        elif cost >= 10:
            quot = cost // 10
            cost = cost % 10
            coin_array[1] += quot
        elif cost >= 5:
            quot = cost // 5
            cost = cost % 5
            coin_array[2] += quot
        elif cost >= 1:
            quot = cost // 1
            cost = cost % 1
            coin_array[3] += quot
    
    all_coin_array.append(coin_array)
         
for i in all_coin_array:
    print(*i)    
