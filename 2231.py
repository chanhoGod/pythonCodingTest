from itertools import permutations

N = int(input())

answer_num = 0

for i in range(1, N + 1):
    # str로 바꿔서 자릿수를 구함
    origin_num = i
    num_arr = list(int(num) for num in str(origin_num))

    if origin_num + sum(num_arr) == N:
        answer_num = origin_num
        break


print(answer_num)