x, y, w, h = map(int, input().split(sep=" "))

tmp_arr = [abs(x - 0), abs(y - 0), abs(x - w), abs(y - h)]

print(min(tmp_arr))
