import sys

read = sys.stdin.readline


N = int(read().strip())

A = list(map(int, read().strip().split()))
R = [0] * N
D = []

for i in range(N):
    # 스택이 비어있지 않고 현재 수열이 스택 top 인덱스가 가리키는 수열보다 큰 경우
    while D and A[D[-1]] < A[i]:
        R[D.pop()] = A[i]
    D.append(i)
    
while D:
    R[D.pop()] = -1

print(*R)