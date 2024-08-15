import sys

N = int(sys.stdin.readline().strip())

num_list = list()

for i in range(N):
    input_num = int(sys.stdin.readline().strip())
    
    if input_num != 0:
        num_list.append(input_num)
    else:
        num_list.pop()

print(sum(num_list))