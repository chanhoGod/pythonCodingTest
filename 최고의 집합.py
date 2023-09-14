def solution(n, s):
    answer = []
    if s / n < 1:
        return [-1]
    
    a = int(s / n)           #몫
    b = s % n           #나머지
    
    numList = list()
    for i in range(n):
        if b == 0:
            numList.append(a)
        else:
            if b > n:
                tmpnum = int(b / n)
                numList.append(a + tmpnum)
                b -= tmpnum
            else:
                numList.append(a + 1)
                b -= 1


    
    return sorted(numList)





print(solution(2, 9))