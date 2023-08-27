def solution(n):
    
    jumpCount = 1
    
    while n > 1:
        if n % 2 != 0:
            n -= 1
            jumpCount += 1
        
        n = n // 2    
    
    return jumpCount



print(solution(5))
print(solution(5000))