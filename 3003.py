white_piece_array = [1, 1, 2, 2, 2, 8]


input_array = list(map(int, input().split(sep=" ")))
tmp_array = [0] * len(input_array)

for i in range(0, len(input_array)):
    tmp_array[i] = white_piece_array[i] - input_array[i]
    
print(*tmp_array)