S = list(input())

numPlace = [-1] * 26
alpabetPlace = [0] * 26

for i in range(0, 26):
    alpabetPlace[i] = chr(97 + i)
    
    
for i in range(0, 26):
    idx = 0
    for j in range(0, len(S)):
        if alpabetPlace[i] != S[j]:
            idx += 1
        else:
            numPlace[i] = idx
            break
        
        
        
for i in numPlace:
    print(i, end=" ")