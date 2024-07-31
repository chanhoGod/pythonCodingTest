N = int(input())

N_length = N * 2 - 1

for i in range(0, N_length):
    space_num1 = N - i - 1

    space_num = abs(space_num1)
    star_num = N_length - space_num * 2
    
    str1 = " " * space_num
    str2 = "*" * star_num
    
    print(str1 + str2)
    