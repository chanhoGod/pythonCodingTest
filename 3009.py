tmp_x = list()
tmp_y = list()

for i in range(3):
    x, y = map(int, input().split(sep=" "))
    
    if x in tmp_x:
        tmp_x.remove(x)
    else:
        tmp_x.append(x)
        
    if y in tmp_y:
        tmp_y.remove(y)
    else:
        tmp_y.append(y)    
    
print(str(tmp_x[0]) + " " + str(tmp_y[0]))