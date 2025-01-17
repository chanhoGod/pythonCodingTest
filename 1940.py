import sys

read = sys.stdin.readline

N = int(read().strip())

M = int(read().strip())

O = list(map(int, read().strip().split()))
O.sort()

start_point = 0
end_point = N - 1
count = 0

while start_point < end_point :
    a = O[start_point]
    b = O[end_point]
    
    if a + b > M :
        end_point -= 1
    elif a + b < M :
        start_point += 1
    elif a + b == M:
        if start_point != end_point:
            count += 1
            end_point -= 1


print(count)