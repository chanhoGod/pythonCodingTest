import sys

N = int(sys.stdin.readline().strip())

N_list = [sys.stdin.readline().strip().split() for i in range(N)]

N_dict = {key:value for key,value in N_list}

answer_list = list()
for key, value in N_dict.items():
    if value == "enter":
        answer_list.append(key)
        

answer_list.sort(reverse=True)

for i in answer_list:
    print(i)