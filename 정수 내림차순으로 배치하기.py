def solution(n):
    return ''.join(sorted(list(map(str, str(n))), reverse=True))


print(solution(118372))