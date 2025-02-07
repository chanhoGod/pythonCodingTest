import math

N = int(input())
maxidx = 1010101
A = [0] * maxidx

def check_pal(num):
    stridx = str(num)
    length = len(stridx)
    start = 0
    end = length - 1
    rtn_flag = False
    if length == 1:
        return True
    
    while start < end:
        if stridx[start] == stridx[end]:
            start +=1
            end -= 1
            rtn_flag = True
            continue
        else:
            rtn_flag = False
            break
    
    return rtn_flag

for i in range(2, maxidx):
    A[i] = i
    

for i in range(2, maxidx):
    
    if A[i] != 0:
        for j in range(i * i, maxidx, i):
            if j % i == 0:
                A[j] = 0

for i in A[N:]:
    if i != 0 and check_pal(i):
        print(i)
        break