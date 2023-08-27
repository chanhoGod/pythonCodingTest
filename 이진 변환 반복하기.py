def solution(s):
    answer = []
    roopingCount = 0
    zeroCount = 0
    
    while s != "1":
        zeroCount += len(s.replace("1", ""))
        roopingCount += 1
        tmpstr = s.replace("0", "")
        int(tmpstr) / 2
        s = format(len(tmpstr), 'b')
            
    answer.append(roopingCount)
    answer.append(zeroCount)
    return answer

print(solution("0111010"))
print(solution("110010101001"))