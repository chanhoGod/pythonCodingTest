def solution(numbers):
    size = len(numbers)
    print(size)
    sortlist = sorted(numbers)
    return int(sortlist[size-1] * sortlist[size-2])



print(solution([1, 2, 3, 4, 5]))