def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a


def lcm(a, b):
    return a*b/gcd(a,b)

a, A = map(int, input().split())
b, B = map(int, input().split())

mom = lcm(A, B)


sun1 = b*(mom/B)
sun2 = a*(mom/A)
sun = sun1 + sun2


print(int(sun / gcd(sun, mom)) , int(mom / gcd(sun, mom))) 
