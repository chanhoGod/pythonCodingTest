
def solution(triangle):
    answer = 0
    
    result = list.copy(triangle)
    triLen = len(triangle)
    
    for i in range(triLen-1, -1, -1):           #i depth
        for j in range(i, -1, -1):       #j lenght
            if i == triLen - 1 :
                result[i][j] = triangle[i][j]
            else:
                result[i][j] = result[i][j] + max(triangle[i+1][j], triangle[i+1][j+1])
    
    print(result)
    return result[0][0]



print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))