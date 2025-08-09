import sys

read = sys.stdin.readline

N = int(read().strip())

N_list = list(map(int, read().split()))

start = 0
end = len(N_list) - 1

max_num = 2000000000
a = 0
b = 0
N_list.sort()

while start < end:
    idx = N_list[start] + N_list[end]
    if abs(idx) < max_num:
        max_num = abs(idx)
        a = N_list[start]
        b = N_list[end]
        
    if idx > 0:
        end -= 1
        continue
    elif idx < 0:
        start += 1
        continue
    else:
        break
    
print(a, b)