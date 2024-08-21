import sys

N = int(sys.stdin.readline())

total_count = 0
user_dict = dict()

for i in range(N):
    str = sys.stdin.readline().strip()
    
    if str == "ENTER":
        user_dict = dict()
    else:
        if str not in user_dict:
            user_dict[str] = 1
            total_count += 1

print(total_count)