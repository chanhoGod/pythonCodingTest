import sys

read = sys.stdin.readline

M = int(read())

O = list(map(int, read().split()))

V = int(read())

result = 0

for i in range(len(O)):
    idx = O[i]
    sumval = sum(O)
    agg = 1
    for j in range(V):
        agg *= idx/sumval
        idx -= 1
        sumval -= 1
    
    result += agg

print(result)