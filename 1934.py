def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)


N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    print(int(lcm(a, b)))