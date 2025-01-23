import sys

read = sys.stdin.readline

N = int(read().strip())

A = [(int(read()), i) for i in range(N)]

max = 0
sorted_A = sorted(A)

for i in range(N):
    if max < sorted_A[i][1] - i:
        max = sorted_A[i][1] - i
    
print(max + 1)