

line_num = 1
max_num = 0
max_index_num = [0, 0]


for i in range(0, 9):
    line = list(map(int, input().split(sep=" ")))
    
    for j in range(0, 9):
        if max_num <= line[j]:
            max_index_num = [i + 1, j + 1]
            max_num = line[j]

print(max_num)
print(*max_index_num)    