def solution(n):
    
    fnList = [1, 1, 1]
    
    for i in range(3, n):
        fnList.append(fnList[i - 1] + fnList[i - 2])
    
    return sum(fnList[:n]) % 1234567
        

print(solution(4))
print(solution(3))
print(solution(10))