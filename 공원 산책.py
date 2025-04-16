def solution(park, routes):
    answer = []
    dx, dy = len(park[0]), len(park)
    O = [['X'] * (dx+2) for i in range(dy+2)] 
    
    for i in range(dy):
        for j in range(dx):
            O[i+1][j+1] = park[i][j]
            if park[i][j] == 'S':
                sx, sy = i+1, j+1
    
    nx, ny = sx, sy
    
    for inst in routes:
        t, d = inst.split()
        if t == 'E':
            px, py = 1, 0
        elif t == 'W':
            px, py = -1, 0
        elif t == 'N':
            px, py = 0, -1
        elif t == 'S':
            px, py = 0, 1
        
        for s in range(int(d)):
            if O[nx + px, ny + py] == 'X':
                break
            else:
                ax, ay = nx+px, ny+py
        
        nx, ny = ax, ay
    print(O)
    return answer

print(solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]))