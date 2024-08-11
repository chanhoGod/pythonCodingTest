import sys
import math

num_list = [int(sys.stdin.readline().strip()) for i in range(5)]

num_list.sort(reverse=False)

print(int(sum(num_list)/len(num_list)))
print(num_list[2])