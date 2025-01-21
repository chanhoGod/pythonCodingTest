import sys

read = sys.stdin.readline

N, M = map(int, read().strip().split())

dna = read().strip()

origin_list = list(map(int, read().strip().split()))
check_list = [0] * 4
cnt = 0

def add_myList(c):
    global check_list
    
    if c == 'A':
        check_list[0] += 1
    elif c == 'C':
        check_list[1] += 1
    elif c == 'G':
        check_list[2] += 1
    elif c == 'T':
        check_list[3] += 1


def sub_myList(c):
    global check_list
    
    if c == 'A':
        check_list[0] -= 1
    elif c == 'C':
        check_list[1] -= 1
    elif c == 'G':
        check_list[2] -= 1
    elif c == 'T':
        check_list[3] -= 1


def compare_list_cnt(A):
    if sum(A) != 0 :
        return False
    else:
        return True

for i in range(0, N):
    if i >= M:
        sub_myList(dna[i - M])
        
    add_myList(dna[i])
    if check_list_cnt(check_list):
        cnt += 1

print(cnt)
