N = int(input())

x_arr = list()
y_arr = list()

for i in range(N):
    x, y = map(int, input().split(sep=" "))
    x_arr.append(x)
    y_arr.append(y)
    
x1 = max(x_arr)
x2 = min(x_arr)
y1 = max(y_arr)
y2 = min(y_arr)

print((x1 - x2) * (y1 - y2))