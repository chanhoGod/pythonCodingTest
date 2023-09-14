def solution(priorities, location):
    newList = list.copy(priorities)
    resultNum = 1
    while len(newList) > 0:
        maxVal = max(newList)

        popVal = newList.pop(0)
        if popVal < maxVal:
            newList.append(popVal)
            if location > 0:
                location -= 1
            else:
                location += (len(newList) - 1)
        else:
            if location == 0:
                return resultNum
            location -= 1
            resultNum += 1

    
    return resultNum





print(solution([2, 1, 3, 4], 3))
print(solution([3, 1, 9, 1, 2, 1], 4))
