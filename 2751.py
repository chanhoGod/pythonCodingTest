import sys

read = sys.stdin.readline
write = sys.stdout.write


# 병합정렬(시작점, 끝점)

def merge_sort(start, end):
    # 크기가 1보다 작은 경우 리턴
    if end - start < 1:
        return
    
    # 중간값 설정
    middle = int(start + (end - start) / 2)
    
    # 분할
    merge_sort(start, middle)
    merge_sort(middle+1, end)
    
    # tmp배열에 값을 임시 저장
    for i in range(start, end + 1):
        O[i] = A[i]
    
    
    k = start
    index1 = start
    index2 = middle + 1
    
    while index1 <= middle and index2 <= end:
        if O[index1] > O[index2]:
            A[k] = O[index2]
            k += 1
            index2 += 1
        else:
            A[k] = O[index1]
            k += 1
            index1 += 1
    
    while index1 <= middle:
        A[k] = O[index1]
        k += 1
        index1 += 1
    
    while index2 <= end:
        A[k] = O[index2]
        k += 1
        index2 += 1
    



N = int(read())
A = [0] * int(N+1)
O = [0] * int(N+1)

for i in range(1, N+1):
    A[i] = int(input())

merge_sort(1, N)

for i in range(1, N+1):
    write(str(A[i]) + '\n')