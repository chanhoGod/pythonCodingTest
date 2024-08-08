import math

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(sep=" "))
    
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue
    
    # 아예 안만날때
    if r1 + r2 < d:
        print(0)
    
    # 외접할때
    elif r1 + r2 == d:
        print(1)
        
    # 교접할때
    elif abs(r1 - r2) < d and d < r1 + r2 :
        print(2)
        
    # 내접할때
    elif abs(r1 - r2) == d:
        print(1)
        
    # 내부에서 안만날때
    elif abs(r1 - r2) > d:
        print(0)
    