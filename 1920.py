import sys

read = sys.stdin.readline


N = int(read())
N_list = sorted(list(map(int, read().split())))
M = int(read())
M_list = list(map(int, read().split()))

def find_num(x):
    start = 0
    end = N-1
    
    while start <= end:
        mid = (start + end) // 2
        
        if N_list[mid] == x:
            return 1
        elif N_list[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    
    return 0


for i in M_list:
    print(find_num(i))