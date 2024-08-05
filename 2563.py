N = int(input())

paper_array = list()
area_num = 0

for i in range(N):
    paper_array.append(list(map(int, input().split(sep=" "))))
    
    
for i in range(0, 100):
    for j in range(0, 100):
        
        for k, l in paper_array:
            if (i >= k and i < k + 10) and (j >= l and j < l + 10):
                area_num += 1
                break


print(area_num)