def solution(arr):
    
    print(gcd(2, 15))
    
    gcdNum = arr[0]
    lcmNum = arr[0]
    
    for i in range(0, len(arr)-1):
        gcdNum = gcd(lcmNum, arr[i+1])
        lcmNum = (lcmNum * arr[i+1]) // gcdNum
        
    return lcmNum


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print(solution([2,6,8,15]))

