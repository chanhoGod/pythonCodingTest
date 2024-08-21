import sys

N, M = map(int, sys.stdin.readline().split())

word_dict = dict()

for i in range(N):
    A = sys.stdin.readline().strip()
    
    if len(A) >= M:
        if A in word_dict:
            word_dict[A] += 1
        else:
            word_dict[A] = 1
            

tuple_list = [(value, key) for key, value in word_dict.items()]

tuple_list.sort(key= lambda x : (-x[0], -len(x[1]), x[1]))

for i in tuple_list:
    print(i[1])
