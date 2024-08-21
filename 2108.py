import sys

N = int(sys.stdin.readline().strip())

num_list = list()

for i in range(N):
    num_list.append(int(sys.stdin.readline().strip()))
    
a = round(sum(num_list) / len(num_list), 0)

sorted_num_list = sorted(num_list)
b = sorted_num_list[int(N/2)]

count_dict = dict()

for i in num_list:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1
max_value = max(count_dict.values())

enu_list = [key for key in count_dict if count_dict[key] == max_value]        

enu_list.sort(key = lambda x : x, reverse=False)

c = 0
if len(enu_list) > 1:
    c = enu_list[1]
else:
    c = enu_list[0]

d = max(num_list) - min(num_list)

print(int(a))
print(b)
print(c)
print(d)