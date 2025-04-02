N = int(input())

A = [0] + list(map(int, input().split()))


L = [0] * (N+2)
R = [0] * (N+2)
L[1] = A[1]
result = L[1]

for i in range(1, N+1):
    L[i] = max(A[i], A[i] + L[i-1])
    result = max(result, L[i])

for i in range(N, 0, -1):
    R[i] = max(A[i], A[i] + R[i+1])
    
for i in range(2, N):
    tmp = L[i-1] + R[i+1]
    result = max(tmp, result)

print(result)