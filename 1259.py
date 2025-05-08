while True:
    num = str(input())
    
    if num == '0':
        break
    
    start = 0
    end = len(num) - 1
    
    while start < end:
        if num[start] != num[end]:
            print('no')
            break
        start += 1
        end -= 1
    
    if start >= end:
        print('yes')
    