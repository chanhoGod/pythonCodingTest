def solution(schedules, timelogs, startday):
    answer = 0
    
    C = [i+10 if i % 100 + 10 < 60 else (i//100+1)*100 + (i % 100 - 50) for i in schedules]
    
    print(C)
    
    for i in range(len(schedules)):
        s_day = startday
        #마감시간
        end_time = C[i]
        
        end_TF = True
        for j in range(7):
            # 만약에 토, 일인경우 제외
            if not ((s_day-1) % 7 == 5 or (s_day-1) % 7 == 6):
                if timelogs[i][j] > end_time:
                    end_TF = False
                    break
            
            s_day += 1
        
        if end_TF:
            answer += 1
    
    return answer



schedules = [759, 800, 1100]
timelogs = [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]]
startday = 5

print(solution(schedules, timelogs, startday))
