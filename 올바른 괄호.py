def solution(s):
    bracketCount = 0
    
    for i in range(0, len(s)):
        if s[i] == "(":
            bracketCount += 1
        elif s[i] == ")":
            bracketCount -= 1
            
        if bracketCount < 0:
            return False
        
    if bracketCount == 0:
        return True
    else:
        return False


print(solution("(())()"))
print(solution(")()("))