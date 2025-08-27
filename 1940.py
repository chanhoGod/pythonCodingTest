import sys

read = sys.stdin.readline

N = int(read())
M = int(read())

O = sorted(list(map(int, read().split())))

start = 0
end = N-1 
result = 0


while start < end:
    first = O[start]
    last = O[end]
    
    if first + last == M:
        result += 1
        start += 1
        end -= 1
    elif first + last > M :
        end -= 1
    elif first + last < M:
        start += 1

print(result)