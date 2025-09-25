import sys

read = sys.stdin.readline

N = int(read())
O = list(map(int, read().split()))
result = [0] * N

for idx, val in enumerate(O):
    cnt = val + 1
    x = 0
    for i in range(len(result)):
        if result[i] == 0:
            cnt -= 1
            if cnt == 0:
                result[i] = idx + 1
    
print(*result)