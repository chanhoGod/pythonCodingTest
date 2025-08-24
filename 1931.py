import sys

read = sys.stdin.readline

N = int(read())

O = [list(map(int, read().split())) for _ in range(N)]
O.sort(key=lambda x:(x[1], x[0]))
result = 0
last_end = 0
for start, end in O:
    
    if start >= last_end:
        result += 1
        last_end = end
        
print(result)