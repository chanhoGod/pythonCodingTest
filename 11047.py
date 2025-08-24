N, K = map(int, input().split())

O = [int(input()) for _ in range(N)]
result = 0
while O:
    coin = O.pop()
    if K < coin:
        continue
    else:
        a = K // coin
        b = K % coin
        K = b
        result += a

print(result)