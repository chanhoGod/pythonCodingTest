import sys

read = sys.stdin.readline

O = str(read()).replace('()', 'X')
stick = 0
result = 0
for i in O:
    if i == '(':
        stick += 1
        result += 1
    elif i == ')':
        stick -= 1
    elif i == 'X':
        result += stick

print(result)