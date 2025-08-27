import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())
S = read().strip()
O = list(map(int, read().split()))

check_list = [0] * 4
start = 0
end = 0
result = 0

def update_count(ch, check_list):
    if ch == 'A':
        check_list[0] += 1
    elif ch == 'C':
        check_list[1] += 1
    elif ch == 'G':
        check_list[2] += 1
    elif ch == 'T':
        check_list[3] += 1

def delete_count(ch, check_list):
    if ch == 'A':
        check_list[0] -= 1
    elif ch == 'C':
        check_list[1] -= 1
    elif ch == 'G':
        check_list[2] -= 1
    elif ch == 'T':
        check_list[3] -= 1

def list_check(check_list):
    for j in range(len(check_list)):
        if check_list[j] < O[j]:
            return False
    return True

for i in range(0, M):
    update_count(S[i], check_list)

if list_check(check_list):
    result += 1

for i in range(M, N):
    new_char = S[i]
    old_char = S[i-M]     
    update_count(new_char, check_list)
    delete_count(old_char, check_list)
    
    if list_check(check_list):
        result += 1

print(result)