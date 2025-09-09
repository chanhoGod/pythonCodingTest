import sys


read = sys.stdin.readline

N = int(read())
O = sorted(list(map(int, read().split())))

result = 0
value = 0
for i in O:
    value += i
    result += value

print(result)