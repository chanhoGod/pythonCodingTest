N = list(input().upper())


tmp_dict = {}

for i in range(0, len(N)):
    if N[i] in tmp_dict:
        tmp_dict[N[i]] = tmp_dict[N[i]] + 1
    else:
        tmp_dict[N[i]] = 1

max_num = 0
max_cnt = 0
tmp_alpha = ""

for i in tmp_dict:
    if max_num < tmp_dict[i]:    
        max_num = tmp_dict[i]
        tmp_alpha = i
        max_cnt = 0
    elif max_num == tmp_dict[i]:
        max_cnt += 1
    
tmp_array = list(tmp_dict.values())
tmp_array.sort()

if max_cnt >= 1:
    print("?")
else :
    print(tmp_alpha)
        
