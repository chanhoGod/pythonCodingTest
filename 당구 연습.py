import math


def solution(m, n, startX, startY, balls):
    answer = []
    
    for xy in balls:
        x = xy[0]
        y = xy[1]
        height = int(math.fabs(y - startY))
        width = int(math.fabs(x - startX))
        
        # 좌 기준
        totalByLeft = pitagorath(x + startX, height)
        
        # 우 기준
        totalByRight = pitagorath(m - x + m - startX, height)

        # 위 기준
        totalByTop = pitagorath(width, n - y + n - startY)
        
        # 아래 기준
        totalByBottom = pitagorath(width,y + startY)
        
        # # # 동일 X선 기준
        # totalByLineX = pitagorath(startY if y > startY else n - startY, startY + height if y > startY else n - startY + height)
        
        # # # 동일 Y선 기준
        # totalByLineY = pitagorath(startX if x > startX else m - startX, startX + width if x > startX else m - startX + width)
        
        print("totalByLeft", totalByLeft)
        print("totalByRight", totalByRight)
        print("totalByTop", totalByTop)
        print("totalByBottom", totalByBottom)
        # print("totalByLineX", totalByLineX)
        # print("totalByLineY", totalByLineY)
        
        
        result = None
        if x == startX:
            result = min(totalByLeft, totalByRight, totalByBottom if y > startY else totalByTop)
        elif y == startY:
            result = min(totalByTop, totalByBottom, totalByLeft if x > startX else totalByRight)
        else:
            result = min(totalByLeft, totalByRight, totalByTop, totalByBottom)
        
        answer.append(result)
        
    return answer

def pitagorath(x, y):
    return x ** 2 + y ** 2


print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3], [4,7]]))
print(solution(10, 10, 0, 0, [[7, 7], [2, 7], [7, 3], [10,10]]))
