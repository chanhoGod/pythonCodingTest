import sys

N = int(sys.stdin.readline())

user_set = set()
user_set.add("ChongChong")
for i in range(N):
    a, b = sys.stdin.readline().strip().split()
    
    
    if a == "ChongChong" or b == "ChongChong":
        if a != "ChongChong" and b == "ChongChong":
            user_set.add(a)
        elif b != "ChongChong" and a == "ChongChong":
            user_set.add(b)
    elif a in user_set and b not in user_set:
        user_set.add(b)
    elif b in user_set and a not in user_set:
        user_set.add(a)


print(len(user_set))