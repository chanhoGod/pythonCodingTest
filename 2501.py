N, K = map(int, input().split(sep=" "))

tmp_array = list()

for i in range(1, N + 1):
    if N % i == 0:
        tmp_array.append(i)
    
    try:
        if tmp_array[K - 1] != None:
            print(tmp_array[K - 1])
            break
    except:
        continue

if len(tmp_array) < K:
    print(0)