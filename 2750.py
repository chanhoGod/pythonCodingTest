N = int(input())

tmp_list = list()

for i in range(N):
    tmp_list.append(int(input()))
    
tmp_list.sort(reverse=False)

for i in tmp_list:
    print(i)