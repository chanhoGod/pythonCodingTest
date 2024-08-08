N = int(input())
num_array = list(map(int, input().split(sep=" ")))

answer_num = 0

for i in num_array:
    A = i
    
    if A == 2 :
        answer_num += 1
        continue
    
    if A == 1 or A % 2 == 0:
        continue
    
    tmp_array = list()
    
    for j in range(1, A + 1):
        if A % j == 0:
            tmp_array.append(j)
    
    if len(tmp_array) == 2:
        answer_num +=1
        

print(answer_num)