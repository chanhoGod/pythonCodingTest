import sys
read = sys.stdin.readline

S = read().strip()
O = S.split('-')

result = sum(map(int, O[0].split('+')))

for i in range(len(O) - 1):
    now_val = O[i+1]
    result -= sum(map(int, now_val.split('+')))

print(result)