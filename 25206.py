

#학점 총합
sum_grade_cnt = 0
sum_major_grade_cnt = 0

major_score = {"A+" : 4.5,
                "A0" : 4.0,
                "B+" : 3.5,
                "B0" : 3.0,
                "C+" : 2.5,
                "C0" : 2.0,
                "D+" : 1.5,
                "D0" : 1.0,
                "F" : 0.0}



for i in range(0, 20):
    subject_list = list(input().split(sep=" "))
    subject_name = subject_list[0]
    subject_grade = float(subject_list[1])
    subject_major = subject_list[2]
    

    
    if subject_major != "P":
       sum_grade_cnt += subject_grade        
       sum_major_grade_cnt += subject_grade * major_score[subject_major]
       
print('%0.6f' %(sum_major_grade_cnt / sum_grade_cnt))
 
    
    