N, M = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b 
    return a

result = gcd(N, M)
print('1' * result)