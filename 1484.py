N = int(input())

start = 1
end = 2
result = []


while start <= N :
    G = end ** 2 - start ** 2
    if G == N:
        result.append(end)
        end += 1
    
    elif G < N:
        end += 1
    else:
        start += 1

if len(result) == 0:
    print(-1)
else:
    for i in sorted(result):
        print(i)