
input_line = 5
long_line_num = 0

matrix_a = list()

for i in range(0, input_line):
    str = list(input())
    if long_line_num < len(str):
        long_line_num = len(str)
    matrix_a.append(str)


str = ""

for i in range(0, long_line_num):
    
        for j in range(0, input_line):
            try:
                str += matrix_a[j][i]
            except:
                continue


print(str)