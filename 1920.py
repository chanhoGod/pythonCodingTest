import sys

read = sys.stdin.readline

N = int(read())

A = list(map(int, read().strip().split()))
A = sorted(A)
M = int(read())
B = list(map(int, read().strip().split()))

for i in range(len(B)):
    find = False
    target = B[i]
    
    start = 0
    end = len(A) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if target > A[mid]:
            start = mid + 1
        elif target < A[mid]:
            end = mid - 1
        elif target == A[mid]:
            find = True
            break
    if find == True:
        print(1)
    else:
        print(0)

