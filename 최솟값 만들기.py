def solution(A,B):
    listA = sorted(A)
    listB = sorted(B, reverse=True)

    returnNumber = 0
    
    for i in range(0, len(listA)):
        returnNumber += listA[i] * listB[i]
    


    return returnNumber





print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1,2], [3,4]))