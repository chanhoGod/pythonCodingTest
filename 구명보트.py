def solution(people, limit):
    
    boatNum = 0
    people = sorted(people)
    left = 0
    right = len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
            
        boatNum += 1
    
    return boatNum




# print(solution([50, 50, 60, 40], 100))
print(solution([50, 40, 80, 70, 60], 150))
print(solution([100, 60, 40, 40], 240))