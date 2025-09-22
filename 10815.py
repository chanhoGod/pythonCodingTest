import sys


read = sys.stdin.readline

N = int(read())
A = sorted(list(map(int, read().split())))

M = int(read())
B = list(map(int, read().split()))

result = []

def binary_search(idx):
    start = 0
    end = len(A) - 1
    
    while start <= end:
        mid = (start + end)//2
        if A[mid] > idx:
            end = mid - 1
        elif A[mid] < idx:
            start = mid + 1
        else:
            return True
    
    return False 
    

for idx in B:
    if binary_search(idx):
        result.append(1)
    else:
        result.append(0)
    
    
print(*result)