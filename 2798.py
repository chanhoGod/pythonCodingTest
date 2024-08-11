N, M = map(int, input().split(sep=" "))

card_list = list(map(int, input().split(sep=" ")))

max_card_sum = 0

for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            card_sum = card_list[i] + card_list[j] + card_list[k]
            
            if card_sum <= M:
                if max_card_sum < card_sum:
                    max_card_sum = card_sum
                    
                    
print(max_card_sum)