def solution(price):
    priceMap = {20:500000, 10:300000, 5:100000}
    
    for key, value in priceMap.items():
        if price >= value:
            print(int(price/100*key))
            print(price/100*key)
            return int(price - price/100*key)
        else :
            continue
    
    return price


print(solution(100010))