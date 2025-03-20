import sys

read = sys.stdin.readline
N, K, P = map(int, read().split())

O = list(map(int, read().split()))

#갯수 체크
cnt = 1
for i in O:
    if i == K:
        cnt += 1

#위치 체크
place = 1
for i in O:
    if i > K:
        place += 1
    else:
        break

# print('place : ', place)
# print('cnt : ', cnt)

if place + cnt - 1 <= P:
    print(place)
else:
    print(-1)