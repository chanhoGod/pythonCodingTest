N = int(input())

for i in range(N):
    A = list(map(int, input().split()))
    
    casenum = A[0]
    
    result = 0
    
    for j in range(1, 20):
        for k in range(j+1, 21):
            if A[j] > A[k]:
                result += 1
    print(casenum, result)
