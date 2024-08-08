import math

T = int(input())

for i in range(T):
    x1, x2, y1, y2 = map(int, input().split(sep=" "))
    N = int(input())
    
    circle_list = list()
    for j in range(N):
        circle_list.append(list(map(int, input().split(" "))))
    
    count = 0

    for j in range(0, len(circle_list)):
        a1 = circle_list[j][0]              #x
        b1 = circle_list[j][1]              #y
        c1 = circle_list[j][2]              #r

        d1 = math.sqrt((x1 - a1) ** 2 + (x2 - b1) ** 2)
        d2 = math.sqrt((y1 - a1) ** 2 + (y2 - b1) ** 2)
        
        r = c1
        
        if r > d1:
            count += 1
        
        if r > d2:
            count += 1
        
        if r > d1 and r > d2:
            count -= 2
            
        
    print(count)