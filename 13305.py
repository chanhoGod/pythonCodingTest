import sys

read = sys.stdin.readline

N = int(read())
S = list(map(int, read().split()))  #street
C = list(map(int, read().split()))  #city

result = 0
min_val = max(C)

for i in range(len(C) - 1):
    min_val = min(min_val, C[i])
    result += min_val * S[i]

print(result)