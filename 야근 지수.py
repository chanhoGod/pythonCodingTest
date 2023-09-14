import heapq

def solution(n, works):
    heapList = []
    heapq.heapify(heapList)
    
    for i in works:
        heapq.heappush(heapList, -1 * i)
    
    
    while n :
        maxValue = -heapq.heappop(heapList)
        if maxValue > 0:
            maxValue -= 1
            heapq.heappush(heapList, -maxValue)
        else :
            heapq.heappush(heapList, 0)
        n -= 1
    rtnValue = sum(i ** 2 for i in heapList)
    return rtnValue



print(solution(8, [10, 7, 9, 2, 2, 9]))
print(solution(4, [4, 3, 3]))
print(solution(8, [1, 1]))




# def solution(n, works):
#     works = sorted(works, reverse=True)    
#     maxNum = max(works)
#     checkCnt = 0
#     while n:
        
#         minusCnt = 0
#         if works[checkCnt] < maxNum:
#             checkCnt += 1
#             maxNum = max(works)
#         else:
#             minusCnt = maxNum - works[checkCnt] + 1
#             if works[checkCnt] > 0:
#                 works[checkCnt] -= minusCnt
#             n -= minusCnt
#             checkCnt += 1
            
        
#         if checkCnt >= len(works):
#             checkCnt = 0
                        
#     answer = sum(i ** 2 for i in works)
    
    
#     return answer
