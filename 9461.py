N = int(input())

# A1 = 1
# A2 = 1
# A3 = 1
# A4 = 2
# A5 = 2
# A6 = 3
# A7 = 4
# A8 = 5
# A9 = 7
# A10 = 9
# A10 = A9 + A5
# A9 = A8 + A4
# A8 = A7 + A3  
# An = An-1 + An-5

n_list = [1, 1, 1, 2, 2]
K = 0

for i in range(5, 100):
    K = n_list[i-1] + n_list[i-5]
    n_list.append(K)


for i in range(N):
    A = int(input())
    print(n_list[A-1])
    