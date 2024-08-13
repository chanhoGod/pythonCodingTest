N, M = map(int, input().split())

N_dict = {key:1 for key in list(map(int, input().split()))}
M_dict = {key:1 for key in list(map(int, input().split()))}

N_list = list()
M_list = list()

for i in N_dict:
    if i not in M_dict:
        N_list.append(i)
        
for i in M_dict:
    if i not in N_dict:
        M_list.append(i)
        

N_len = len(N_list)
M_len = len(M_list)

print(N_len + M_len)