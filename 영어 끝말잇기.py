def solution(n, words):

    lastSpell = words[0][0]
    mytimes = 1
    wordsNum = 0
    
    dupList = []

    for i in words:
        wordsNum += 1
        myNum = wordsNum % n + n if wordsNum % n == 0 else wordsNum % n
        mytimes = wordsNum // n + 1 if wordsNum % n > 0 else wordsNum // n
        
        if i in dupList:
            return [myNum, mytimes]
        
        if i[0] != lastSpell:
            return [myNum, mytimes]
        
        lastSpell = i[-1]
        dupList.append(i)

    return [0, 0]



print(solution(3, ["tank", "kank", "kank", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))