N, M = map(int, input().split())

N_list = [input().strip() for i in range(N)]
N_dict = {key:1 for key in N_list}

M_list = [input().strip() for i in range(M)]

answer_num = 0

for i in M_list:
    if i in N_dict:
        answer_num += 1
        

print(answer_num)