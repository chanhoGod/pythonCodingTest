import sys

N, k = map(int, input().split())

num_list = list(map(int, sys.stdin.readline().strip().split()))

num_list.sort(reverse=True)

print(num_list[k-1])