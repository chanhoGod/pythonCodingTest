import sys

read = sys.stdin.readline
A = read().strip().split('-')

result = 0

for i in range(len(A)):
    sum_num = sum(list(map(int, A[i].split('+'))))
    
    if i == 0:
        result += sum_num
    else:
        result -= sum_num

print(result)