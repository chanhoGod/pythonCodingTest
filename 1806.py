import sys

read = sys.stdin.readline

N, S = map(int, read().split())

N_list = list(map(int, read().split()))


left = 0
right = 0
sum_value = 0
size = float('inf')

while right < N:
    sum_value += N_list[right]
    right += 1

    while sum_value >= S:
        size = min(size, right-left)
        sum_value -= N_list[left]
        left += 1

if size == float('inf'):
    print(0)
else:
    print(size)