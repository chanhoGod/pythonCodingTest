import sys
from collections import Counter

read = sys.stdin.readline

N, d, k, c = map(int, read().split())

N_list = [int(read().strip()) for i in range(N)]
sushi_list = [0] * (d+1)
left = 0
count = 0

# 초기 설정
for i in range(k):
    sushi_list[N_list[i]] += 1
    if sushi_list[N_list[i]] == 1:
        count += 1

result = count + (1 if sushi_list[c] == 0 else 0)

while left < N:
    old_sushi = N_list[left]
    sushi_list[old_sushi] -= 1
    
    if sushi_list[old_sushi] == 0:
        count -= 1
    
    new_sushi = N_list[(left + k) % N]
    sushi_list[new_sushi] += 1
    if sushi_list[new_sushi] == 1:
        count += 1

    tmp_result = count + (1 if sushi_list[c] == 0 else 0)

    result = max(result, tmp_result)
    left += 1

print(result)