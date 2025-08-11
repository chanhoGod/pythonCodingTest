import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(read())

N_list = list(map(int, read().split()))

op_list = list(map(int, read().split()))

max_value = float('-inf')
min_value = float('inf')

def sumVal(a, b):
    return a + b

def subVal(a, b):
    return a - b

def mulVal(a, b):
    return a * b

def divVal(a, b):
    if a < 0:
        return -(-a // b)
    else:
        return a // b


def dfs(depth, value):
    global max_value, min_value
    if depth == N:
        max_value = max(max_value, value)
        min_value = min(min_value, value)
        return
    
    next_num = N_list[depth]
    
    if op_list[0] > 0:
        op_list[0] -= 1
        dfs(depth+1, sumVal(value, next_num))
        op_list[0] += 1
    if op_list[1] > 0:
        op_list[1] -= 1
        dfs(depth+1, subVal(value, next_num))
        op_list[1] += 1
    if op_list[2] > 0:
        op_list[2] -= 1
        dfs(depth+1, mulVal(value, next_num))
        op_list[2] += 1
    if op_list[3] > 0:
        op_list[3] -= 1
        dfs(depth+1, divVal(value, next_num))
        op_list[3] += 1

dfs(1, N_list[0])

print(max_value)
print(min_value)