import math
N = int(input())

N_list = list()
tree_list = list()

prev_tree = 0

for i in range(0, N):
    tree = int(input())
    tree_list.append(tree)
    tmp_space = tree - prev_tree
    prev_tree = tree
    if i > 0:
        N_list.append(tmp_space)
    
space = math.gcd(*N_list)


min_tree = min(tree_list)
max_tree = max(tree_list)


print(int((max_tree - min_tree) / space - N + 1))