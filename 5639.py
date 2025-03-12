import sys
sys.setrecursionlimit(10**6)
L = []

while True:
    try:
        stridx = int(sys.stdin.readline().rstrip())
        L.append(stridx)
    except:
        break

def pre_order(array):
    if len(array) == 0:
        return
    
    left = []
    right = []
    mid = array[0]
    
    for i in range(1, len(array)):
        if array[i] < mid:
            left.append(array[i])
        elif array[i] > mid:
            right.append(array[i])
        else:
            continue
    
    pre_order(left)
    pre_order(right)
    print(mid)
    

pre_order(L)