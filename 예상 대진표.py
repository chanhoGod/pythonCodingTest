def solution(n,a,b):
    answer = 0
        
    while a != b:
        a = int((a + 1) / 2);
        b = int((b + 1) / 2);
        answer += 1;

    return answer
    


print(solution(8, 3, 4))
print(solution(8, 4, 7))
print(solution(8, 4, 5))