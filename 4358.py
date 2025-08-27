import sys

read = sys.stdin.readline

D = dict()
cnt = 0
while True:
    tree = read().strip()
    if tree != '':
        cnt += 1
        if tree not in D:
            D[tree] = 1
        else:
            D[tree] += 1
    else:
        break

for key in sorted(D.keys()):
    value = D[key]/cnt*100
    print("%s %.4f" %(key, value))