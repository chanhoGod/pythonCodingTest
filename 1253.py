import sys

read = sys.stdin.readline

N = int(read().strip())

O = list(map(int, read().strip().split()))
O.sort()

count = 0

for i in range(N):
    k = O[i]
    s = 0
    e = N - 1
    while e > s:
        if O[s] + O[e] == k:
            if s != i and e != i:
                count += 1
                break
            elif s == i:
                s += 1
            elif e == i:
                e -= 1
        elif O[s] + O[e] > k:
            e -= 1
        elif O[s] + O[e] < k:
            s += 1
            
print(count)