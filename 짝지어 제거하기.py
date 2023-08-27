def solution(s):
    strList = list()
    
    for i in s:
        strList.append(i)
        
        if len(strList) >= 2 and  strList[-1] == strList[-2]:
            strList.pop()
            strList.pop()
    
    if len(strList) > 0:
        return 0
    else: return 1    




print(solution("baabaa"))
print(solution("cdcd"))