import sys

N = int(sys.stdin.readline().strip())

N_list = list()

for i in range(N):
    tmp_str = sys.stdin.readline().strip().split(' ')
    fnc = tmp_str[0]

    if len(tmp_str) > 1 :
        num = tmp_str[1]
        
        if fnc == 'push':
            N_list.append(num)
        
    else:
        if fnc == 'top':
            if len(N_list) >= 1:
                print(N_list[-1])
            else:
                print(-1)
        elif fnc == 'size':
            print(len(N_list))
        elif fnc == 'empty':
            if len(N_list) >= 1:
                print(0)
            else:
                print(1)
        elif fnc == 'pop':
            if len(N_list) >= 1:
                popnum = N_list.pop(-1)
                print(popnum)
            else:
                print(-1)
        
        
        