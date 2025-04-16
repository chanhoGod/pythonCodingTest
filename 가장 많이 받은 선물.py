def solution(friends, gifts):
    answer = 0
    
    
    # 이번달까지 두사람 사이에 더 많은 선물을 준 사람이 다음달에 선물을 하나 받음
    
    # 주고받은게 없거나 횟수가 같으면 선물지수가 큰 사람이 낮은사람에게 선물을 하나 받음
    
    
    
    return answer



friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

print(solution(friends, gifts))