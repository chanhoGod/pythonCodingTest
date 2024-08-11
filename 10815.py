import sys

N = int(sys.stdin.readline().strip())



input_num_list = list(map(int, sys.stdin.readline().strip().split()))
has_num_list = {key:1 for key in input_num_list}

M = int(sys.stdin.readline().strip())

compare_num_list = list(map(int, sys.stdin.readline().strip().split()))

for i in range(0, len(compare_num_list)):
    if compare_num_list[i] in has_num_list:
        compare_num_list[i] = 1
    else:
        compare_num_list[i] = 0


print(*compare_num_list)