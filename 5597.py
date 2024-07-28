import sys

studentCount = 30

studentArray = [0] * studentCount


for i in range(0, studentCount - 2):
    N = int(sys.stdin.readline())
    studentArray[N - 1] = N

for i in range(len(studentArray)):
    if studentArray[i] == 0:
        print(i+1)
    