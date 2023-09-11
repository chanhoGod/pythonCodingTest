def solution(s):
    answer = 0
    
    newStr = s
    
    for i in range(0, len(s)):
        newStr = newStr[1:] + newStr[0]
        tmpStr = newStr  
        while True:
            if "()" in tmpStr:
                tmpStr = tmpStr.replace("()", "")
            elif "{}" in tmpStr:
                tmpStr = tmpStr.replace("{}", "")
            elif "[]" in tmpStr:
                tmpStr = tmpStr.replace("[]", "")
            else:
                break
        

        if len(tmpStr) == 0:
            answer += 1
            

    return answer



print(solution("[](){}"))