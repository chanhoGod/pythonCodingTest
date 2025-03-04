import sys

read = sys.stdin.readline

N = int(read())
M = int(read())

O = [i for i in range(N+1)]

def find(val):
    if O[val] != val:
        O[val] = find(O[val])
        return O[val]
    else:
        return val

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        O[b] = a


for i in range(1, N+1):
    
    A = list(map(int, read().strip().split()))
    for j in range(1, len(A)+1):
        if A[j-1] == 1:
            union(i, j)

M_list = list(map(int, read().strip().split()))

tf_flag = True
for i in range(len(M_list)-1):
    if find(M_list[i]) != find(M_list[i+1]):
        print("NO")
        tf_flag = False
        break

if tf_flag == True:
    print("YES")
