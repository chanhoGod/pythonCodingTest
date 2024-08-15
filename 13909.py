import math

N= int(input())

cnt = 0

for i in range(1, int(math.sqrt(N)) + 1):
    cnt += 1

print(cnt)