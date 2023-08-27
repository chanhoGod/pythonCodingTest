def solution(s):
    returnList = []
    tmpstr = s.replace(" ", "-")
    print(tmpstr)
    setList = list(tmpstr.split("-"))
    for i in setList:
        tmpText = ""
        for j in range(0, len(i)):
            if j == 0:
                # print(i[j].upper())
                tmpText+= i[j].upper()
            else:
                # print(i[j].lower())
                tmpText+= i[j].lower()
                            
        returnList.append(tmpText)
        if i != setList[len(setList) - 1]:
           returnList.append("-")
        # print(tmpText)
        
        
    return "".join(i for i in returnList).replace("-", " ")


print(solution("ppp  pp  p  ppPPPP"))
print(solution("3people unFollowed me"))
print(solution("pP"))
print(solution("   pp     ppp      PPP"))