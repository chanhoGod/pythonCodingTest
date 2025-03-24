N, M = map(int, input().split())

O = list(map(int, input().split()))

start_point = 0
end_point = 0
result = 0
sumval = 0
while end_point <= N:
    if sumval == M:
        sumval -= O[start_point]
        start_point += 1
        result += 1    
    elif sumval > M:
        sumval -= O[start_point]
        start_point += 1
    elif sumval < M:
        if end_point >= N:
            break
        else:
            sumval += O[end_point]
            end_point += 1

print(result)