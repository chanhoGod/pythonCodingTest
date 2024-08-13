import math

def find_primeNumber(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    
    return True
    

N = int(input())

for i in range(N):
    num = int(input())
    while True:
        if num == 0 or num == 1:
            num += 1
        else:  
            if find_primeNumber(num) == False:
                num += 1
            else:
                print(num)
                break