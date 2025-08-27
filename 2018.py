N = int(input())


start = 1
end = 1
result = 1
sum_value = 0

while start <= N//2:
    
    while sum_value <= N:
        if sum_value == N:
            result += 1
        sum_value += end
        end += 1
    
    while sum_value > N:
        sum_value -= start
        start += 1
    

print(result)