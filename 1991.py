N = int(input())

O = {}

for i in range(N):
    root, left, right = input().split()
    O[root] = [left, right]

def pre_order(node):
    if node == ".":
        return
    print(node, end="")
    pre_order(O[node][0])
    pre_order(O[node][1])

def in_order(node):
    if node == ".":
        return
    in_order(O[node][0])
    print(node, end="")
    in_order(O[node][1])
    
def post_order(node):
    if node == ".":
        return 
    post_order(O[node][0])
    post_order(O[node][1])
    print(node, end="")
    

pre_order("A")
print()
in_order("A")
print()
post_order("A")
