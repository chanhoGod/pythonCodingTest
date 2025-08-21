N = int(input())
result = 0

def check_str(S):
    D = dict()
    last_str = ''

    for k in S:
        if k not in D:
            D[k] = 1
            last_str = k
        else:
            if last_str != k:
                return False
    
    return True

for i in range(N):
    S = str(input().strip())
    if check_str(S):
        result += 1


print(result)    