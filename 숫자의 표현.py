def solution(n):
    answer = 0
    
    numList = [i for i in range(1, n + 1)]
    

    for i in range (1, n + 1):
        sumnum = 0
        for j in range(i , n + 1):
            sumnum += j
            if sumnum == n:
                answer += 1
                break
            elif sumnum > n:
                break
            

    
    return answer



print(solution(15))
print(solution(19))