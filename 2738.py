N, M = map(int, input().split(sep=" "))

matrixA = list()
matrixB = list()


#A배열 넣기
for i in range(N):
    line = map(int, input().split(sep=" "))
    matrixA.append(line)

#B배열 넣기
for i in range(N):
    line = map(int, input().split(sep=" "))
    matrixB.append(line)

answer_matrix = list()
for i in range(0, N):
    answer_matrix.append([x + y for x, y in zip(matrixA[i], matrixB[i])])

for i in answer_matrix:
    print(*i)
