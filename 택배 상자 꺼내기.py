def solution(n, w, num):
    answer = 1
    
    A = [[0] * w for _ in range((n // w) + 1)]
    x = 0
    y = 0
    for i in range(n):
        # 짝수층 0, 2, 4 ->
        if (i//w) % 2 == 0:
            A[i//w][i%w] = i+1
            if i+1 == num:
                x = i//w
                y = i%w
        # 홀수층 1, 3, 5 <-
        else:
            A[i//w][w - i%w - 1] = i+1
            if i+1 == num:
                x = i//w
                y = w - i%w - 1
    print(A)
    
    print(x, y)
    for i in range(x+1, len(A)):
        if A[i][y] != 0:
            answer +=1
    print(answer)
    return answer

solution(22, 6, 8)
solution(13, 3, 6)
solution(2, 1, 1)
solution(3, 2, 1)
solution(9, 3, 6)