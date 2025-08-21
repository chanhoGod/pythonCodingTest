import sys


read = sys.stdin.readline

N, C = map(int, read().split())
O = [int(read()) for _ in range(N)]
sorted_O = sorted(O)

start = 1
end = sorted_O[-1] - sorted_O[0]
result = 0

def can_install(mid):
    count = 1
    last_installed = sorted_O[0]
    
    for i in range(1, N):
        if sorted_O[i] - last_installed >= mid:
            count += 1
            last_installed = sorted_O[i]
            if count >= C:
                return True
    return False

while start <= end:
    mid = (start + end) // 2
    
    if can_install(mid):
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)