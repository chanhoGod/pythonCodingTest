import sys

read = sys.stdin.readline

N = int(read())

A = [0] + list(map(int, read().split()))
O = [0] * (N + 1)


cnt = 0

def merge_sort(start, end):
    global cnt
    if end - start < 1:
        return

    # 비교 값들 설정
    middle = int(start + (end - start) / 2)
    
    merge_sort(start, middle)
    merge_sort(middle+1, end)
    
    index1 = start
    index2 = middle + 1
    k = start

    # 임시 배열값 설정, 매 분할마다 설정해주어서 값을 유동적으로 바꿀 수 있게 해줘야 함
    for i in range(start, end + 1):
        O[i] = A[i]

    # 각각의 값이 분할의 끝 기준과 비교해서 작은 경우에 진행, 각 인덱스의 값을 비교해서 조건에 맞을경우 스왑
    while index1 <= middle and index2 <= end:
        if O[index1] > O[index2]:
            A[k] = O[index2]
            cnt = cnt + index2 - k
            k += 1
            index2 += 1
        else:
            A[k] = O[index1]
            k += 1
            index1 += 1
    
    # 나머지 처리 안된 값들 처리
    while index1 <= middle:
        A[k] = O[index1]
        k += 1
        index1 += 1
    
    while index2 <= end:
        A[k] = O[index2]
        k += 1
        index2 += 1
        
merge_sort(1, N)
print(cnt)