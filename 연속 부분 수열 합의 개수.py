def solution(elements):
    
    setList = set()
    elLen = len(elements)
    for i in range(1, elLen+1):
        tmpInt = 0
        while tmpInt < elLen:
            if elLen >= tmpInt+i:
                setList.add(sum(elements[tmpInt:tmpInt+i]))
            else:
                newElements = elements[tmpInt:] + elements[:tmpInt]
                setList.add(sum(newElements[0:i]))
            tmpInt += 1

    
    print(setList)
    
    return len(setList)



print(solution([7,9,1,1,4]))