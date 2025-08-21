import sys


read = sys.stdin.readline

N = str(read().strip()).upper()
D = dict()

for i in N:
    if i in D:
        D[i] += 1
    else:
        D[i] = 1
result = ''
result_cnt = 0
for key, value in D.items():
    max_num = max(D.values())
    if value == max_num:
        result_cnt += 1
        if result_cnt > 1:
            print('?')
            exit()
        result = key

print(result)