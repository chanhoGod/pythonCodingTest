S = input()

start = 0
end = 1

sentence_set = set()

while end <= len(S):
    if start + end <= len(S): 
        sentence_set.add(S[start : start + end])
        start += 1
    else:
        start = 0
        end += 1


print(len(sentence_set))