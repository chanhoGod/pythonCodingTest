
while True:
    n = int(input())
    
    if n == -1:
        break
    
    tmp_array = list()
    
    for i in range(1, n):
        if n % i == 0:
            tmp_array.append(i)
    
    if sum(tmp_array) == n :
        output_str = str(n) + " = "
        num_arr = " + ".join(map(str, tmp_array))
        output_str = output_str + num_arr
        
        print(output_str)
    else:
        print(str(n) + " is NOT perfect.")