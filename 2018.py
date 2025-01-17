# 투포인터 문제
# 시작점과 끝점을 계산해서 결과가 합보다 작으면 end++, 결과가 합보다 크면 start++

import sys

readline = sys.stdin.readline

N = int(readline().strip())

start_point = 1
end_point = 2
n = 1
count = 0

while start_point <= N :
    
    if n == N :
        count += 1
        n -= start_point
        start_point += 1
    elif n > N :
        n -= start_point
        start_point += 1
    elif n < N :
        n += end_point
        end_point += 1
    

print(count)