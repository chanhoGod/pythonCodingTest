N = int(input())
A = list(map(int, input().split()))

def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

def next_permutation(A):
    
    # next_permutation
    # 1. 뒤에서부터 검색, i < i+1인경우 i값 체크
    # 2. i값을 제외하고 뒤에서부터 다시 검색할때 i보다 큰 노드와 i값을 스왑
    # 3. 스왑한 값 이후 들어오는 값에 대해 오름차순으로 sort한다음 붙이기
    for i in range(N-2, -1, -1):
        if A[i] < A[i+1]:
            x = i
            for j in range(N-1, x, -1):
                if A[j] > A[x]:
                    swap(A, j, x)
                    A = A[:x+1] + sorted(A[x+1:])
                    print(*A)
                    exit()

next_permutation(A)
print(-1)