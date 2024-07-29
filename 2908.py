a, b = list(input().split())

a = a[::-1]
b = b[::-1]

intA = int(a)
intB = int(b)

if intA > intB:
    print(intA)
else:
    print(intB)