N, B = map(int, input().split())

base_str = ""

while N > 0:

    mod = N % B    
    N = N // B
    
    if mod > 9:
        base_str += chr(55 + mod)
    else:
        base_str += str(mod)

print(base_str[::-1])
    
    