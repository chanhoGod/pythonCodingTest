N = int(input())

answer = 0
index = 2
tmp_num = 1

for i in range(1, N + 1):
    index += tmp_num
    answer = index * index
    tmp_num *= 2
    
print(answer)