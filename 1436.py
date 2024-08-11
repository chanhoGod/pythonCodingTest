import math

N = int(input())

sixsixsix = "666"
num = 666
count = 1

num_list = [num]

while True:
    
    if sixsixsix in str(num):
        num_list.append(num)
    
    num += 1
    
    if len(num_list) > N:
        break

print(num_list[-1])