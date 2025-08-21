import sys

read = sys.stdin.readline

N = int(read())

N_list = []

for i in range(N):
    line = read().split()

    if line[0] == 'push':
        N_list.append(int(line[1]))
    elif line[0] == 'pop':
        if len(N_list) == 0:
            print(-1)
        else:
            print(N_list.pop())
    elif line[0] == 'size':
        print(len(N_list))
    elif line[0] == 'empty':
        if len(N_list) == 0:
            print(1)
        else:
            print(0)
    elif line[0] == 'top':
        print(N_list[-1] if N_list else -1)

