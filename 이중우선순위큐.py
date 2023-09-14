def solution(operations):
    
    resultList = list()
    maxValue = 0
    minValue = 0
    for i in operations:
        if i[0] == "I":
            resultList.append(int(i[2:]))
            if len(resultList) == 0:
                maxValue = 0
                minValue = 0
            else:
                maxValue = max(resultList)
                minValue = min(resultList)
        elif i == "D -1":
            if len(resultList) > 0:
                resultList.remove(minValue)
                if len(resultList) == 0:
                    maxValue = 0
                    minValue = 0
                else:
                    maxValue = max(resultList)
                    minValue = min(resultList)
        elif i == "D 1":
            if len(resultList) > 0:
                resultList.remove(maxValue)
                if len(resultList) == 0:
                    maxValue = 0
                    minValue = 0
                else:
                    maxValue = max(resultList)
                    minValue = min(resultList)
            
    
    return [max(resultList), min(resultList)] if len(resultList) > 0 else [0, 0]



# print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "I 653", "D 1", "D 1", "D 1", "D 1", "D 1", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))