S = list(input())

dial = [[''], ['ABC'], ['DEF'], ['GHI'], ['JKL'], ['MNO'], ['PQRS'], ['TUV'], ['WXYZ'], ['']]

sum = 0

for i in range(0, len(S)):
    sum += 1
    for j in range(0, len(dial)):
        if S[i] in list(dial[j][0]):
            break
        sum += 1
    sum += 1
    
print(sum)