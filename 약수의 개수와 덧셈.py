def solution(left, right):
    answer = 0
    numberMap = {}
    
    for i in range(left, right + 1):
        numberList = []
        for j in range(1, i+1):
            if i % j == 0:
                numberList.append(j)
        numberMap[i] = numberList

    for i in numberMap:
        if len(numberMap.get(i)) % 2 == 0:
            answer += i
        else:
            answer -= i
        
    return answer



print(solution(24, 27))