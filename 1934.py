def gcd(a, b):
    while True:
        c = b % a
        if c == 0:
            return a
        else:
            b = a
            a = c
            

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    gcd_num = gcd(a, b)
    
    result = int(b * a / gcd_num)
    print(result)