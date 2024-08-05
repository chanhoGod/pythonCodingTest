N = int(input())

# 입력한 라인수 만큼의 각각의 크기는 100
# 각자의 넓이의 총합에서 겹친 부분을 제외하게 되면 검은 부분의 넓이가 나올것

max_area = N * 100

point_array = list()

for i in range(0, N):
    point_array.append(list(map(int, input().split(sep=" "))))

for i in range(0, N - 1):
    a = point_array[i][0]
    b = point_array[i][1]

    c = point_array[i+1][0]
    d = point_array[i+1][1]
    
    x = 0
    y = 0
    
    if a < c + 10 or c < a + 10:
        x = abs(c + 10 - a) 
        print("x : ", x)
    
    if b < d + 10 or d < b + 10:
        y = abs(d + 10 - b)
        print("y : ", y)
        
    tmp_area = x * y
    
    max_area -= tmp_area

print(max_area)
