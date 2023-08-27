import math

def solution(price, money, count):
    
    for i in range(1, count + 1):
        print('money : ',money)
        print('count : ',i)
        if money <= 0:
            break

        money -= (price * i)        
        


    return 0 if money >= 0 else int(math.fabs(money))

print(solution(1, 1, 2))