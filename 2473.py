import sys

read = sys.stdin.readline

N = int(read())
N_list = sorted(map(int, read().split()))

max_value = float('inf')

result = []

for i in range(N-2):
    start = i+1
    end = N-1
    
    while start < end:
        idx = N_list[i] + N_list[start] + N_list[end]
        abs_idx = abs(idx)
        if max_value > abs_idx:
            max_value = abs_idx
            result = [N_list[i], N_list[start], N_list[end]]
        if idx > 0:
            end -= 1
        elif idx < 0:
            start += 1
        else:
            print(N_list[i], N_list[start], N_list[end])
            exit(0)
        
print(*result)