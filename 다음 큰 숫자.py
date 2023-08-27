def solution(n):
    
    originBinnum = makeBinary(n)
    originNumBinLen = len(originBinnum.replace("0", ""))
    n += 1
    while True:
        binnum = makeBinary(n)
        if originNumBinLen != len(binnum.replace("0", "")):
            n += 1
        else:
            return n
    

def makeBinary(num):
    strbin = ""
    while num != 1:
        tmpN = int(num % 2)
        num //= 2
        strbin += (str(tmpN))
    
    strbin += "1"
    reversebin = strbin[::-1]
    
    return reversebin

print(solution(78))
print(solution(15))
print(solution(957483))