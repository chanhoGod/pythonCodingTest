N = int(input())

three_array = [i * 3 for i in range(N // 3 + 1)]
five_array = [i * 5 for i in range(N // 5 + 1)]

answer = 5000

for i in range(0, len(three_array)):
    for j in range(0, len(five_array)):
        tmp_num = three_array[i] + five_array[j]
        if tmp_num == N:
            if answer > i + j:
                answer = i + j

if answer == 5000:
    print(-1)
else:
    print(answer)