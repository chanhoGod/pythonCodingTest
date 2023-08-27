def solution(number, n, m):
        
    return 1 if (int(number%n) == 0 and int(number%m) == 0)  else 0




print(solution(55, 10, 5))
print(solution(60, 10, 7))
print(solution(77, 10, 5))