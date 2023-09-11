def solution(k, tangerine):
    answer = 0
    
    fruitDic = {}
    
    for i in tangerine:
        if fruitDic.get(i) == None:
            fruitDic[i] = 1
        else: fruitDic[i] += 1
    
    print(fruitDic)

    sortedFruit = dict(sorted(fruitDic.items(), key=lambda x:x[1], reverse=True))
    
    for i in sortedFruit:
        if k <= 0:
            return answer
        print("num: ",i)
        k -= sortedFruit[i]
        answer += 1
    
    return answer







print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
# print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
# print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))
