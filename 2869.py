import math

A, B, V = map(int, input().split(sep=" "))

C = V - B
D = A - B


    
print(math.ceil(C / D))