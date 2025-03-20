def findleg(O, heart, core):
    x, y = heart
    x = x + core
    
    leftleg = 0
    rightleg = 0
    
    for i in range(x+1, len(O)):
        if O[i][y-1] == '*':
            leftleg += 1
    
    for i in range(x+1, len(O)):
        if O[i][y+1] == '*':
            rightleg += 1

    return leftleg, rightleg

def findcore(O, heart):
    x, y = heart
    core = 0
    for i in range(x+1, len(O)):
        if O[i][y] == '*':
            core += 1
    return core

def findarm(O, heart):
    x, y = heart
    
    leftarm = 0
    for i in O[x][:y]:
        if i == '*':
            leftarm += 1
    
    rightarm = 0
    for i in O[x][y+1:]:
        if i == '*':
            rightarm += 1
    
    return leftarm, rightarm

def findheart(head):
    x, y = head
    return (x+1, y)

def findhead(O):
    for i in range(len(O)):
        for j in range(len(O[i])):
            if O[i][j] == '*':
                return (i, j)

N = int(input())

O = [[''] * (N+1) for i in range(N+1)]
for i in range(1, N+1):
    a = list(input())
    
    for j in range(1, N+1):
        O[i][j] = a[j-1]

head = findhead(O)
heart = findheart(head)
leftarm, rightarm = findarm(O, heart)
core = findcore(O, heart)
leftleg, rightleg = findleg(O, heart, core)

print(heart[0], heart[1])
print(leftarm, rightarm, core, leftleg, rightleg)