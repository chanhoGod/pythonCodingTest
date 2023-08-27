def solution(brown, yellow):
    brownWidth = 0
    brownHeight = 0
    
    yellowWidth = 0
    yellowHeight = 0
    
    argnumList = getArgs(yellow)
    
    for i in argnumList:
        yellowWidth = i
        yellowHeight = yellow // i
        
        brownWidth = yellowWidth + 2
        brownHeight = yellowHeight
        
        if brownWidth * 2 + brownHeight * 2 == brown:
            return [brownWidth, brownHeight + 2]
    
    answer = []
    return answer

def getArgs(num):
    returnNumList = list()
    
    for i in range(1, num + 1):
        if num % i == 0:
            returnNumList.append(i)

    return returnNumList[::-1]



print(solution(10, 2))
print(solution(24, 24))