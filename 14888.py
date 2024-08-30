def calculate(a, answer_num):
    global max_num
    global min_num
    
    if a == len(N_list) - 1:
        max_num = max(answer_num, max_num)
        min_num = min(answer_num, min_num)
        
    if operators[0] != 0:
        operators[0] -=1
        calculate(a+1, answer_num + N_list[a+1])
        operators[0] +=1
        
    if operators[1] != 0:
        operators[1] -=1
        calculate(a+1, answer_num - N_list[a+1])
        operators[1] +=1
        
    if operators[2] != 0:
        operators[2] -=1
        calculate(a+1, answer_num * N_list[a+1])        
        operators[2] +=1
        
    if operators[3] != 0:
        operators[3] -=1
        calculate(a+1, int(answer_num / N_list[a+1]))        
        operators[3] +=1
            
N = int(input())

max_num = -(1000000000)
min_num = 1000000000
answer = 0

N_list = list(map(int, input().split()))
operators = list(map(int, input().split()))

calculate(0, N_list[0])
print(max_num)
print(min_num)