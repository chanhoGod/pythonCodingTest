def solution(n):
    
    fnList = [0, 1]
    
    for i in range(2, n + 1):
        if i <= n:
            fnList.append(fnList[i - 1] + fnList[i - 2])
            
    
    return fnList[n] % 1234567



print(solution(3))
print(solution(5))