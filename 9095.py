T = int(input())

for i in range(T):
    
    
    N = int(input())
    target_list = [0] * (12)
    target_list[1] = 1
    target_list[2] = 2
    target_list[3] = 4
    if N > 3:
        for i in range(4, N+1):
            target_list[i] = target_list[i-1] + target_list[i-2] + target_list[i-3]
    
    print(target_list[N])