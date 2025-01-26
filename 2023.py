import sys


read = sys.stdin.readline
outs = sys.stdout.write

N = int(read())

def find_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

def dfs(a):
    if len(str(a)) == N:
        outs(str(a) + '\n')
    else:
        for i in range(1, 10):
            k = a * 10 + i
            if k % 2 == 1 and find_prime(k) == True:
                dfs(k)

dfs(2)
dfs(3)
dfs(5)
dfs(7)