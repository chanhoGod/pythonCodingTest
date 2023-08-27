def solution(s):
    return str(min(list(map(int, s.split())))) + " " + str(max(list(map(int, s.split()))))


print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))