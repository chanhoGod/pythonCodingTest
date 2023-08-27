def solution(slice, n):
    return int(n/slice + 1) if n % slice > 0 else int(n/slice)



print(solution(14, 7))