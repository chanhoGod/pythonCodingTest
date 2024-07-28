def input_ball(a, b, c, array):
    
    # 배열
    for tmp in range(a - 1, b):
        array[tmp] = c


i, j = map(int, input().split())

# print(i, j)

array = [0] * i

for i in range(j):
    a, b, c = map(int, input().split())
    input_ball(a, b, c, array)

for i in array:
    print(i,  end=' ')


