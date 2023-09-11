def solution(n, left, right):
    answer = []
    
    arrArr = [[[0 for _ in range(n)] for _ in range(n)]]
    
    for i in range(0, n):
        for j in arrArr[i]:
            if i == 1 or j == 1:
                arrArr[i][j] = 1
        

    
    return answer




print(solution(3, 2, 5))