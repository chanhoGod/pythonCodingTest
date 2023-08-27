def solution(num_list, n):
    returnList = []
    for i in range(0, n):
        returnList.append(num_list[i])
    return returnList;


def solution2(num_list, n):                 #개고수넹.....
    return num_list[:n]


print(solution([2, 1, 6] ,1))
print(solution([5, 2, 1, 7, 5] ,3))