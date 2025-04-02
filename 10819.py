from itertools import permutations
N = int(input())

A = list(map(int, input().split()))

result = 0

# 모든 순열을 생성한 뒤에 각각의 차이를 계산하여 최댓값 업데이트
for per in permutations(A):
    tmp_sum = 0
    
    for i in range(N-1):
        tmp_sum += abs(per[i] - per[i+1])

    result = max(result, tmp_sum)

print(result)