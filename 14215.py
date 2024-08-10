A, B, C = map(int, input().split(sep=" "))

tmp_arr = list([A, B, C])
tmp_arr.sort(reverse=True)

max_num = tmp_arr[0]
min_num_sum = sum(tmp_arr[1:])

while True:
    if max_num >= min_num_sum:
        max_num -= 1
    else:
        print(max_num + min_num_sum)
        break