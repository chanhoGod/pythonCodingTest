
while True:
    str = input()
    
    if str[0] == '.':
        break
    
    big_bracket_cnt = 0
    small_bracket_cnt = 0
    rtn_boo = False
    bracket_stack = list()
    
    for i in str:
        if i == "(":
            bracket_stack.append("s")
            small_bracket_cnt += 1
        elif i == "[":
            bracket_stack.append("b")
            big_bracket_cnt += 1
        
        
        if i == ")":
            if len(bracket_stack) == 0:
                print("no")
                rtn_boo = True
                break
            
            pop_str = bracket_stack.pop()                            
            if pop_str == "b":
                print("no")
                rtn_boo = True
                break
            elif pop_str == "s":
                small_bracket_cnt -= 1

        elif i == "]":
            if len(bracket_stack) == 0:
                print("no")
                rtn_boo = True
                break
        
            pop_str = bracket_stack.pop()   
            
            if pop_str == "s":
                print("no")
                rtn_boo = True
                break
            elif pop_str == "b":
                big_bracket_cnt -= 1

        if small_bracket_cnt < 0 or big_bracket_cnt < 0:
            print("no")
            rtn_boo = True
            break
    
    if small_bracket_cnt == 0 and big_bracket_cnt == 0 and rtn_boo == False:
        print("yes")
    elif (small_bracket_cnt > 0 or big_bracket_cnt > 0) and rtn_boo == False:
        print("no")
            
        
    