N, M = map(int, input().split())

rtn_dict = dict()

for i in range(N):
    str = input()
    
    if str not in rtn_dict:
        rtn_dict[str] = 1
    else:
        rtn_dict[str] += 1
        

for i in range(M):
    str = input()
    
    if str not in rtn_dict:
        rtn_dict[str] = 1
    else:
        rtn_dict[str] += 1

rtn_cnt = 0
rtn_list = list()
for key, value in rtn_dict.items():
    if value > 1:
        rtn_cnt += 1
        rtn_list.append(key)
        

print(rtn_cnt)
rtn_list.sort(reverse=False)

for i in rtn_list:
    print(i)