N = int(input())

for i in range(N):
    str = input()
    
    cnt = 0
    
    for j in str:
        if j == "(":
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            print("NO")
            break
        
    
    if cnt == 0:
        print("YES")
    elif cnt > 0:
        print("NO")
    