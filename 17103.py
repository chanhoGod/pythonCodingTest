import math, sys

def prime_number_list(a):
    prime_list = [i for i in range(a+1)]
    
    for i in range(2, int(math.sqrt(a)) + 1):
        if prime_list[i] == 0:
            continue
        for j in range(i * i, a+1, i):
            prime_list[j] = 0

    prime_list[0] = 0
    prime_list[1] = 0
    
    return prime_list

def find_partition(prime_number_list, M):
    cnt = 0
    for i in prime_number_list:
        if i >= M:
            break
        
        otherNum = M - i
        if otherNum in prime_number_list:
            cnt += 1
    
    if cnt % 2 == 1:
        cnt = cnt // 2 + 1
    else:
        cnt = cnt // 2
    
    return cnt

N = int(sys.stdin.readline().strip())

prime_list = prime_number_list(1000000)

for i in range(N):
    M = int(sys.stdin.readline().strip())

    print(find_partition(prime_list, M))