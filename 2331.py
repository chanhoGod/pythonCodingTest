A, P = map(int, input().split())

O = dict()
O[A] = 1

lastnum = A
while True:
    idxlist = list(map(int, str(lastnum)))
    
    num = 0
    for i in idxlist:
        num += i ** P
    
    lastnum = num
    if num not in O:
        O[num] = 1
    else:
        if O[num] == 3:
            break
        O[num] += 1

cnt = 0
for i in O.keys():
    if O[i] == 1:
        cnt+=1

print(cnt)