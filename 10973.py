N = int(input())

A = list(map(int, input().split()))

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def prev_permutation(A):
    
    # prev_permutation
    # 1. i > i + 1인경우 i값 체크
    # 2. 체크한 i값을 기준으로 j값이 i보다 작은 경우 swap
    # 3. 체크한 i값 이후의 값들을 내림차순으로 정렬 
    for i in range(N-2, -1, -1):
        if A[i] > A[i+1]:
            x = i
            for j in range(N-1, x, -1):
                if A[x] > A[j]:
                    swap(A, x, j)
                    A = A[:x+1] + sorted(A[x+1:], key=lambda x:-x)
                    print(*A)
                    exit()

prev_permutation(A)
print(-1)