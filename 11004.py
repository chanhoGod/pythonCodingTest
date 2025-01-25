import sys

read = sys.stdin.readline

N, K = map(int, read().split())

A = list(map(int, read().strip().split()))

def partition(start, end, arr):
    #시작점을 start로 잡음
    #피벗은 첫번째 인덱스
    pivot_index = (start + end) // 2
    pivot = arr[pivot_index]
    
    #end가 start보다 큰 경우
    while start <= end:
        
        while arr[start] < pivot:
            start += 1
            
        while arr[end] > pivot:
            end -= 1
        
        if start <= end:
            # 값 교환
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1    
    
    return start

def quick_sort(arr, start, end):
    if start < end:
        # Partition 배열을 분할하고, 피벗의 최종 위치를 얻음
        pivot_index = partition(start, end, arr)
        
        # 왼쪽 부분 배열 재귀 호출
        quick_sort(arr, start, pivot_index - 1)
        # 오른쪽 부분 배열 재귀 호출
        quick_sort(arr, pivot_index + 1, end)
    


quick_sort(A, 0, N - 1)
print(A[K-1])

# sorted_A = sorted(A)

# print(sorted_A[K-1])
