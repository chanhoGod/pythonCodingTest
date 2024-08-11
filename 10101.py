a = int(input())
b = int(input())
c = int(input())

sum_num = a + b + c

if a == 60 and b == 60 and c == 60:
    print("Equilateral")
elif (a == b or b == c or c == a) and sum_num == 180:
    print("Isosceles")
elif (a != b and b != c and c != a) and sum_num == 180:
    print("Scalene")
elif sum_num != 180:
    print("Error")