import sys

read = sys.stdin.readline
vowellist = ['a', 'e', 'i', 'o', 'u']
while True:
    sentence = read().strip()
    
    if sentence == "end":
        break
    
    #모음 포함
    invowel = False
    for i in sentence:
        if i in vowellist:
            invowel = True
    
    if not invowel:
        print(f"<{sentence}> is not acceptable.")
        continue
    
    #연속 2개 안됨
    nextTF = True
    for i in range(len(sentence) - 1):
        now = sentence[i]
        next = sentence[i+1]
        if now == next:
            if now in ['e', 'o'] and next in ['e', 'o']:
                continue
            else:
                nextTF = False
                break
    if not nextTF:
        print(f"<{sentence}> is not acceptable.")
        continue
    
    #모음 혹은 자음 연속 3개 안됨
    sequenceTF = True
    cnt = 1
    for i in range(len(sentence) - 2):
        now = sentence[i]
        next = sentence[i+1]
        mnext = sentence[i+2]
        
        if now in vowellist and next in vowellist and mnext in vowellist:
            sequenceTF = False
            break
        
        if now not in vowellist and next not in vowellist and mnext not in vowellist:
            sequenceTF = False
            break
    if not sequenceTF:
        print(f"<{sentence}> is not acceptable.")
        continue
    
    print(f"<{sentence}> is acceptable.")

