import math

def prime_number(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    
    return True

N, M = map(int, input().split())

for i in range(N, M + 1):
    if i == 1:
        continue
    
    if prime_number(i) == True:
        print(i)
