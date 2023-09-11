def solution(gems):
    uniqueGems = set(gems)
    uniqueGemsLen = len(uniqueGems)
    
    tmpGemsDict = dict()
    
    gemLength = 1000001
    start = 0
    end = 0
    
    returnEnd = 0
    returnStart = 0
    
    while end < len(gems):
        if gems[end] not in tmpGemsDict:
            tmpGemsDict[gems[end]] = 0
        tmpGemsDict[gems[end]] += 1
        
        if len(tmpGemsDict) == uniqueGems:
            
        
        end += 1
    
    return [returnStart, returnEnd]
    
# def solution(gems):   
    
#     print(gems)
#     gemsMap = dict()
#     uniqueGemsLen = len(set(gems))
    
#     maxCount = 0
#     minCount = 0
#     length = 100001    
#     for i in range(0, len(gems)):
#         if gems[i] in gemsMap:
#             gemsMap[gems[i]] = i + 1
#         else:
#             gemsMap[gems[i]] = i + 1    
        
#         if len(gemsMap.keys()) == uniqueGemsLen:
#             tmpmax = i + 1
#             tmpmin = min(gemsMap.values())
#             if length > tmpmax - tmpmin:
#                 length = tmpmax - tmpmin
#                 maxCount = tmpmax
#                 minCount = tmpmin
            
    
#     print(gemsMap)
                
    

#     return [minCount, maxCount]


print(solution(["E", "E", "A", "B", "C", "D", "D", "D", "D", "D", "E", "F", "B" ,"C", "A"]))
print(solution(["A", "B", "B", "B", "C", "D", "D", "D", "D", "D", "D", "D", "B" ,"C", "A"]))
print(solution(["DIA", "RUBY", "EMERALD", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AB", "AC", "AB", "AC", "AA", "AB", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
