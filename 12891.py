def word_count(tmpstr, A):
    
    for i in tmpstr:
        if i == 'A':
            A[0] -= 1
        elif i == 'C':
            A[1] -= 1
        elif i == 'G':
            A[2] -= 1
        elif i == 'T':
            A[3] -= 1
        
        if A[0] <= 0 and A[1] <= 0 and A[2] <= 0 and A[3] <= 0:
            return True
    
    return False

def list_count(A):
    if A[0] <= 0 and A[1] <= 0 and A[2] <= 0 and A[3] <= 0:
        return True

N, M = map(int, input().split())

O = list(input())
A = list(map(int, input().split()))

cnt = 0
tmp_str = O[:M]
if word_count(tmp_str, A):
    cnt += 1

for i in range(0, N-M):
    s = tmp_str[0]
    e = O[M+i]
    if s == 'A':
        A[0] += 1
    elif s == 'C':
        A[1] += 1
    elif s == 'G':
        A[2] += 1
    elif s == 'T':
        A[3] += 1
    
    if e == 'A':
        A[0] -= 1
    elif e == 'C':
        A[1] -= 1
    elif e == 'G':
        A[2] -= 1
    elif e == 'T':
        A[3] -= 1
    tmp_str.pop(0)
    tmp_str.append(e)
    if list_count(A):
        cnt += 1

print(cnt)