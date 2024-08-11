while True:
    A, B, C = map(int, input().split(sep=" "))

    if A == 0 and B == 0 and C == 0:
        break
    
    tmp_arr = list([A, B, C])
    tmp_arr.sort(reverse=True)
    max_num = tmp_arr[0]
    
    min_num_sum = sum(tmp_arr[1:])
    
    if max_num >= min_num_sum:
        print("Invalid") 
    elif A == B == C:
        print("Equilateral")
    elif A == B or B == C or C == A:
        print("Isosceles")
    elif A != B != C :
        print("Scalene")
    
    