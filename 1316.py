def check_sentense_cnt(str):
    rtnbln = True
    
    nowChar = ""
    tmp_dict = dict()
    
    
    for i in str:

        if i not in tmp_dict:
            tmp_dict[i] = 1
        else:
            if i == nowChar:
                tmp_dict[i] += 1
            else:
                rtnbln = False
                break
            
        nowChar = i
    
    
    return rtnbln

N = int(input())
S = 0


for i in range(N):
    str = input()
    if check_sentense_cnt(str) == True:
        S += 1


print(S)