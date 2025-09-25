def solution(n, w, num):
    answer = 0
    height = n//w if n % w == 0 else (n // w) + 1
    
    O = [[0] * w for _ in range(height)]
    col = 0
    for i in range(n):
        x = (i // w)
        if x % 2 == 0:
            y = (i % w) 
        else:
            y = w - (i % w) -1
            
        O[x][y] = i + 1
        
        if i+1 == num:
            col = y
    print(O)
    for i in range(len(O)-1, -1, -1):
        if O[i][col] != 0:
            answer += 1
            if O[i][col] == num:
                break
    print(answer)
    return answer

solution(22, 6, 8)
solution(13, 3, 6)
solution(2, 1, 1)
solution(3, 2, 1)
solution(9, 3, 6)