import math

def prime_number(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
        
    return True

prime_num_list = set()

while True:
    num = int(input())
    cnt = 0
    end_num = num * 2 + 1
    if num != 0:
        for i in range(num + 1, end_num):
            if i in prime_num_list:
                cnt+=1
                continue
            
            if prime_number(i) == True:
                prime_num_list.add(i)
                cnt += 1
    else:
        break
    
    print(cnt)