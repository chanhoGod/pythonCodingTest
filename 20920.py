import sys

read = sys.stdin.readline

N, M = map(int, read().split())
D = dict()
for i in range(N):
    word = read().strip()
    if len(word) >= M:
        if word not in D:
            D[word] = 1
        else:
            D[word] += 1

D = sorted(D, key=lambda x: (-D[x], -len(x), x))
for i in D:
    print(i)