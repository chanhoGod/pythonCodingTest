N = input()

a = 1

for i in range(0, int(len(N) / 2) + 1):
    if N[i] != N[len(N) - i - 1]:
        a = 0

print(a)
