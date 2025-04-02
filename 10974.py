N = int(input())

A = [i for i in range(1, N +1)]


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def next_permutation(A):
    for i in range(N-2, -1, -1):
        if A[i] < A[i+1]:
            x = i
            for j in range(N-1, x, -1):
                if A[x] < A[j]:
                    swap(A, x, j)
                    A[x+1:] = sorted(A[x+1:])
                    return False
    
    return True

print(*A)

while not next_permutation(A):
    print(*A)