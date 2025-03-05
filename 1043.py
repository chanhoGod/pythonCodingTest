import sys

read = sys.stdin.readline

N, M = map(int, read().strip().split())

T = list(map(int, read().strip().split()))
TN = T[0]
TP = T[1:]

O = [i for i in range(N+1)]

def find(val):
    if O[val] != val:
        O[val] = find(O[val])
        return O[val]
    elif O[val] == val:
        return val

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        O[b] = a
        if a in TP:
            TP.append(b)
        elif b in TP:
            TP.append(a)

total_idx_list = list()

for i in range(M):
    A = list(map(int, read().strip().split()))
    num = A[0]
    idx_list = A[1:]
    total_idx_list.append(idx_list)
    if num > 1:
        for j in range(len(idx_list) - 1):
            union(idx_list[j], idx_list[j+1])

rtn_num = M

for i in range(len(total_idx_list)):
    tmp_list = total_idx_list[i]
    for j in range(len(tmp_list)):
        target = tmp_list[j]
        if find(target) in TP:
            rtn_num -= 1
            break

print(rtn_num)